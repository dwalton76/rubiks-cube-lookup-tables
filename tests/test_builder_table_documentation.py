"""AST-only enforcement for documentation on retained lookup-table builders."""

# standard libraries
import ast
import re
from dataclasses import dataclass, field
from pathlib import Path

# third party libraries
import pytest

PACKAGE = Path(__file__).resolve().parents[1] / "rubikscubelookuptables"
BUILDER_MODULES = tuple(PACKAGE / f"builder{size}.py" for size in (333, 444, 555, 666, 777))
HISTOGRAM_MARKERS = (" steps has ", "Total:", "Average:")
STICKER_LINE = re.compile(r"^\s*(?:[.xULFRBD1-]\s+){2,}[.xULFRBD1-]\s*$")
LOOKUP_NAME = re.compile(r"lookup-table-[A-Za-z0-9_.+-]+")


@dataclass
class TableClass:
    """One retained concrete table class discovered from builder AST."""

    path: Path
    name: str
    lineno: int
    kind: str
    docstring: str
    bases: tuple
    node: ast.ClassDef | None = None
    attrs: dict = field(default_factory=dict)
    private_ancestors: tuple = ()
    inherited_diagram_count: int = 0


def _module_ast(path):
    return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def _classes(tree):
    return [node for node in tree.body if isinstance(node, ast.ClassDef)]


def _base_names(node):
    names = []
    for base in node.bases:
        if isinstance(base, ast.Name):
            names.append(base.id)
        elif isinstance(base, ast.Attribute):
            names.append(base.attr)
    return tuple(names)


def _const_str(node):
    return node.value if isinstance(node, ast.Constant) and isinstance(node.value, str) else None


def _eval_string_tuple(node, env):
    if isinstance(node, ast.Name) and node.id in env:
        return env[node.id]
    if isinstance(node, (ast.Tuple, ast.List)):
        values = []
        for elt in node.elts:
            if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                values.append(elt.value)
            else:
                return None
        return tuple(values)
    return None


def _class_attrs(node):
    attrs = {}
    for stmt in node.body:
        if not isinstance(stmt, ast.Assign):
            continue
        if len(stmt.targets) != 1:
            continue
        target = stmt.targets[0]
        if isinstance(target, ast.Name):
            value = _const_str(stmt.value)
            if value is not None:
                attrs[target.id] = value
        elif isinstance(target, ast.Tuple) and isinstance(stmt.value, ast.Tuple):
            for left, right in zip(target.elts, stmt.value.elts):
                if isinstance(left, ast.Name):
                    value = _const_str(right)
                    if value is not None:
                        attrs[left.id] = value
    return attrs


def _calls_bfs_init(node):
    init = next(
        (
            item
            for item in node.body
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)) and item.name == "__init__"
        ),
        None,
    )
    if init is None:
        return False
    return any(
        isinstance(call.func, ast.Attribute)
        and call.func.attr == "__init__"
        and isinstance(call.func.value, ast.Name)
        and call.func.value.id == "BFS"
        for call in ast.walk(init)
        if isinstance(call, ast.Call)
    )


def _is_public_build_name(name):
    return name.startswith("Build") and not name.startswith("StartingStates")


def _is_private_base_name(name):
    return name.startswith("_Build")


def _is_starting_states_name(name):
    return name.startswith("StartingStates")


def _ancestor_names(name, by_name, seen=None):
    seen = set() if seen is None else seen
    node = by_name.get(name)
    if node is None or name in seen:
        return ()
    seen.add(name)
    names = []
    for base in _base_names(node):
        names.append(base)
        names.extend(_ancestor_names(base, by_name, seen))
    return tuple(names)


def _private_ancestors(name, by_name):
    return tuple(base for base in _ancestor_names(name, by_name) if _is_private_base_name(base))


def _module_env_string_tuples(tree):
    env = {}
    for stmt in tree.body:
        if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name):
            value = _eval_string_tuple(stmt.value, env)
            if value is not None:
                env[stmt.targets[0].id] = value
    return env


def _spec_function_rows(tree, func_name, env):
    func = next(
        (node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == func_name),
        None,
    )
    if func is None:
        return ()
    for node in ast.walk(func):
        if not isinstance(node, ast.GeneratorExp):
            continue
        if len(node.generators) != 1:
            continue
        iterator = _eval_string_tuple(node.generators[0].iter, env)
        if iterator is None:
            continue
        rows = []
        for value in iterator:
            local = dict(env)
            if isinstance(node.generators[0].target, ast.Name):
                local[node.generators[0].target.id] = value
            if isinstance(node.elt, ast.Tuple):
                row = []
                for elt in node.elt.elts:
                    if isinstance(elt, ast.Name) and elt.id in local:
                        row.append(local[elt.id])
                    elif isinstance(elt, ast.JoinedStr):
                        parts = []
                        for part in elt.values:
                            if isinstance(part, ast.Constant):
                                parts.append(str(part.value))
                            elif isinstance(part, ast.FormattedValue) and isinstance(part.value, ast.Name):
                                parts.append(str(local.get(part.value.id, "")))
                            else:
                                parts = None
                                break
                        if parts is None:
                            row = None
                            break
                        row.append("".join(parts))
                    elif isinstance(elt, ast.Constant):
                        row.append(elt.value)
                    else:
                        row = None
                        break
                if row is not None:
                    rows.append(tuple(row))
        if rows:
            return tuple(rows)
    return ()


def _dict_str_values(node):
    if not isinstance(node, ast.Dict):
        return {}
    values = {}
    for key, value in zip(node.keys, node.values):
        key_name = _const_str(key)
        value_name = _const_str(value)
        if key_name is not None and value_name is not None:
            values[key_name] = value_name
        elif isinstance(key, ast.Constant) and key.value in {"axis", "table_slug"} and isinstance(value, ast.Name):
            values[key.value] = value.id
    return values


def _dynamic_wrappers(path, tree, by_name):
    env = _module_env_string_tuples(tree)
    tables = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name) or node.func.id != "type":
            continue
        if len(node.args) < 3:
            continue
        bases = []
        if isinstance(node.args[1], ast.Tuple):
            bases = [elt.id for elt in node.args[1].elts if isinstance(elt, ast.Name)]
        private_bases = tuple(base for base in bases if _is_private_base_name(base))
        if not private_bases:
            continue
        attrs = _dict_str_values(node.args[2])
        class_names = []
        if isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
            class_names = [node.args[0].value]
        elif isinstance(node.args[0], ast.Name):
            for parent in ast.walk(tree):
                if not isinstance(parent, ast.For):
                    continue
                if not (
                    isinstance(parent.target, ast.Tuple)
                    and any(isinstance(elt, ast.Name) and elt.id == node.args[0].id for elt in parent.target.elts)
                ):
                    continue
                if not isinstance(parent.iter, ast.Call) or not isinstance(parent.iter.func, ast.Name):
                    continue
                rows = _spec_function_rows(tree, parent.iter.func.id, env)
                name_index = next(
                    (
                        index
                        for index, elt in enumerate(parent.target.elts)
                        if isinstance(elt, ast.Name) and elt.id == node.args[0].id
                    ),
                    None,
                )
                slug_index = next(
                    (
                        index
                        for index, elt in enumerate(parent.target.elts)
                        if isinstance(elt, ast.Name) and elt.id == "slug"
                    ),
                    None,
                )
                axis_index = next(
                    (
                        index
                        for index, elt in enumerate(parent.target.elts)
                        if isinstance(elt, ast.Name) and elt.id == "axis"
                    ),
                    None,
                )
                for row in rows:
                    resolved = dict(attrs)
                    if name_index is not None and name_index < len(row):
                        class_names.append(row[name_index])
                    if slug_index is not None and slug_index < len(row) and "table_slug" in attrs:
                        resolved["table_slug"] = (
                            row[slug_index] if attrs.get("table_slug") == "slug" else attrs["table_slug"]
                        )
                    if axis_index is not None and axis_index < len(row) and attrs.get("axis") == "axis":
                        resolved["axis"] = row[axis_index]
                    if class_names:
                        name = class_names[-1]
                        if not _is_public_build_name(name):
                            continue
                        tables.append(
                            TableClass(
                                path=path,
                                name=name,
                                lineno=node.lineno,
                                kind="wrapper",
                                docstring="",
                                bases=tuple(bases),
                                attrs=resolved if "table_slug" in resolved or "axis" in resolved else attrs,
                                private_ancestors=private_bases,
                            )
                        )
                class_names = []
        for name in class_names:
            if _is_public_build_name(name):
                tables.append(
                    TableClass(
                        path=path,
                        name=name,
                        lineno=node.lineno,
                        kind="wrapper",
                        docstring="",
                        bases=tuple(bases),
                        attrs=attrs,
                        private_ancestors=private_bases,
                    )
                )
    unique = {}
    for table in tables:
        unique[table.name] = table
    return tuple(unique.values())


def _is_visual_diagram(text):
    lines = text.splitlines()
    sticker_lines = sum(bool(STICKER_LINE.match(line)) for line in lines)
    return sticker_lines >= 3


def _inline_diagrams(node):
    if node is None:
        return []
    doc_expr = node.body[0] if node.body and isinstance(node.body[0], ast.Expr) else None
    doc_value = doc_expr.value if doc_expr is not None else None
    diagrams = []
    for value in ast.walk(node):
        if value is doc_value:
            continue
        if isinstance(value, ast.Constant) and isinstance(value.value, str) and _is_visual_diagram(value.value):
            diagrams.append(value.value)
    return diagrams


def _diagram_on_node(node, docstring):
    return int(_is_visual_diagram(docstring)) + len(_inline_diagrams(node))


def _private_base_diagram_count(by_name, ancestor_names):
    count = 0
    for name in ancestor_names:
        node = by_name.get(name)
        if node is None:
            continue
        count += _diagram_on_node(node, ast.get_docstring(node, clean=True) or "")
    return count


def _table_classes_for_module(path):
    tree = _module_ast(path)
    class_nodes = _classes(tree)
    by_name = {node.name: node for node in class_nodes}
    tables = []
    for node in class_nodes:
        if _is_starting_states_name(node.name) or _is_private_base_name(node.name):
            continue
        if not _is_public_build_name(node.name):
            continue
        private = _private_ancestors(node.name, by_name)
        if _calls_bfs_init(node):
            kind = "direct"
        elif private:
            kind = "wrapper"
        else:
            continue
        tables.append(
            TableClass(
                path=path,
                name=node.name,
                lineno=node.lineno,
                kind=kind,
                docstring=ast.get_docstring(node, clean=True) or "",
                bases=_base_names(node),
                node=node,
                attrs=_class_attrs(node),
                private_ancestors=private,
                inherited_diagram_count=_private_base_diagram_count(by_name, private),
            )
        )
    for table in _dynamic_wrappers(path, tree, by_name):
        table.inherited_diagram_count = _private_base_diagram_count(by_name, table.private_ancestors)
        tables.append(table)
    by_table_name = {table.name: table for table in tables}
    return tuple(by_table_name[name] for name in sorted(by_table_name))


def _all_table_classes():
    tables = []
    for path in BUILDER_MODULES:
        tables.extend(_table_classes_for_module(path))
    return tuple(tables)


def _has_histogram(doc):
    return all(marker in doc for marker in HISTOGRAM_MARKERS)


def _identifies_concrete_table(table):
    blob = " ".join(
        [
            table.docstring,
            table.name,
            " ".join(str(value) for value in table.attrs.values()),
        ]
    )
    if LOOKUP_NAME.search(blob):
        return True
    slug = table.attrs.get("table_slug")
    return isinstance(slug, str) and bool(slug)


def _documentation_errors(table):
    errors = []
    own_diagrams = _diagram_on_node(table.node, table.docstring)
    if table.kind == "direct":
        missing = [marker.strip() for marker in HISTOGRAM_MARKERS if marker not in table.docstring]
        if missing:
            errors.append(f"docstring is missing {', '.join(missing)}")
        if own_diagrams == 0:
            errors.append("table has no cube diagram in its docstring or inline starting state")
        elif own_diagrams > 1:
            errors.append(
                "cube diagram is duplicated; keep one diagram in the docstring or one inline starting state, not both"
            )
        return errors

    if not _identifies_concrete_table(table):
        errors.append("wrapper does not identify its concrete table via lookup-table name or table_slug")
    if not _has_histogram(table.docstring):
        errors.append("concrete table is missing its own authoritative histogram (steps has / Total: / Average:)")

    inherited_diagrams = table.inherited_diagram_count
    if own_diagrams and inherited_diagrams:
        errors.append(
            "cube diagram is duplicated on the wrapper and its private base; keep the shared coordinate diagram on the base"
        )
    elif own_diagrams == 0 and inherited_diagrams == 0:
        errors.append("wrapper has no cube diagram of its own and none on a private _Build* base")
    elif own_diagrams > 1:
        errors.append(
            "cube diagram is duplicated; keep one diagram in the docstring or one inline starting state, not both"
        )
    return errors


def _builder_cases():
    for table in _all_table_classes():
        yield pytest.param(table, id=f"{table.path.stem}.{table.name}")


@pytest.mark.parametrize("table", tuple(_builder_cases()))
def test_concrete_builder_table_documentation_is_normalized(table):
    errors = _documentation_errors(table)
    assert not errors, f"{table.path.name}:{table.lineno} {table.name}: " + "; ".join(errors)


def test_builder_classification_separates_helpers_abstract_bases_and_wrappers():
    kinds = {}
    for path in BUILDER_MODULES:
        tree = _module_ast(path)
        table_by_name = {table.name: table.kind for table in _table_classes_for_module(path)}
        names = {}
        for node in _classes(tree):
            if node.name.startswith(("Build", "_Build", "StartingStates")):
                names[node.name] = table_by_name.get(node.name)
        for table in _table_classes_for_module(path):
            names.setdefault(table.name, table.kind)
        kinds[path.stem] = names

    assert kinds["builder555"]["Build555Phase4"] == "direct"
    assert kinds["builder555"]["StartingStatesBuild555Phase4"] is None
    assert kinds["builder666"]["_Build666DaisyInnerXSpineCenters"] is None
    assert kinds["builder777"]["_Build777DaisyCenters"] is None
    assert kinds["builder777"]["_Build777Phase56UDPairStage"] is None
    assert kinds["builder777"]["_Build777SolveCenters"] is None
    assert kinds["builder777"]["Build777DaisyUDWithoutLeftObliqueCenters"] == "wrapper"
    assert kinds["builder777"]["Build777Phase56UDLeftRightObliqueCentersStage"] == "wrapper"
    assert kinds["builder777"]["Build777DaisyPerfectCenters"] == "wrapper"
    assert kinds["builder777"]["Build777SolvePerfectCenters"] == "wrapper"
    assert kinds["builder666"]["Build666DaisyAllInnerXPlusUDObliquesCenters"] == "wrapper"
    assert kinds["builder666"]["Build666DaisyAllInnerXPlusLRObliquesCenters"] == "wrapper"
    assert kinds["builder666"]["Build666DaisyAllInnerXPlusFBObliquesCenters"] == "wrapper"


def test_wrapper_docs_may_inherit_shared_diagram_but_not_histogram():
    tree = ast.parse('''
class _BuildExample(BFS):
    """
        . U .
        U . U
        . U .
    """
    def __init__(self):
        BFS.__init__(self)

class BuildExampleLeaf(_BuildExample):
    """lookup-table-example.txt"""
    table_slug = "example"
''')
    by_name = {node.name: node for node in _classes(tree)}
    leaf = by_name["BuildExampleLeaf"]
    table = TableClass(
        path=Path("builder_example.py"),
        name=leaf.name,
        lineno=leaf.lineno,
        kind="wrapper",
        docstring=ast.get_docstring(leaf, clean=True) or "",
        bases=_base_names(leaf),
        node=leaf,
        attrs=_class_attrs(leaf),
        private_ancestors=("_BuildExample",),
        inherited_diagram_count=_diagram_on_node(
            by_name["_BuildExample"],
            ast.get_docstring(by_name["_BuildExample"], clean=True) or "",
        ),
    )
    errors = _documentation_errors(table)
    assert any("authoritative histogram" in error for error in errors)
    assert not any("no cube diagram" in error for error in errors)


def test_inline_diagram_rule_detects_duplicate_locations():
    tree = ast.parse('''
class BuildExample:
    """
        . U .
        U . U
        . U .
    """
    pattern = """
        . U .
        U . U
        . U .
    """
''')
    node = tree.body[0]
    assert _is_visual_diagram(ast.get_docstring(node))
    assert len(_inline_diagrams(node)) == 1
