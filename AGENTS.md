# Agent handbook: rubiks-cube-lookup-tables

Python + C BFS/IDA builders for the prune tables consumed by `../rubiks-cube-NxNxN-solver`. This repo is **not** the solver. Finished production tables already live on S3 (`https://rubiks-cube-lookup-tables.s3.amazonaws.com/`).

## Rules

- Do **not** start a production table build unless the user explicitly asks. Full ranked tables take many CPU-hours and can fill RAM/tmpfs. Makefile targets such as `666-phase5`, `777-daisy-perfect` are real jobs, not smoke tests.
- Do **not** commit unless the user asks. Do not force-push or skip hooks.
- Never point tests at `lookup-tables/`. Pytest must set `RUBIKS_LOOKUP_TABLE_DIR=tmp/test-lookup-tables` and `RUBIKS_SKIP_HISTOGRAM=1` (`make test` already does).
- Do not run builder tests with pytest-xdist. Builders share `./tmp`.
- Do not format or commit generated `rubikscubelookuptables/builder555ss.py` / `builder777ss.py` (tens of MB, gitignored).
- Builders import `rubikscubennnsolver`. After `make init`, `PYTHONPATH` must include the solver repo.
- Project skills in `.cursor/skills/`: never CRLF (always LF); never keep unused lookup-table code in either repo; if a phase is slow, sample a heuristic matrix instead of shipping `--multiplier`.

## Layout

| Path | Role |
| --- | --- |
| `rubikscubelookuptables/builder{333,444,555,666,777}.py` | Builder classes (`Build444LRCentersStageRanked`, …) |
| `rubikscubelookuptables/buildercore.py` | Search, ranked mmap, save, histogram, JSON sidecars |
| `rubikscubelookuptables/builder-crunch-workq.c` | C work-queue expander used by Python builders |
| `rubikscubelookuptables/builder-find-new-states.c` | Frontier helper |
| `utils/builderui.py` | CLI: `./utils/builderui.py BuildXxx [--depth N] [--cores N]` |
| `utils/build-ida-graph.py` | Convert a builder’s JSON graph for the solver |
| `utils/json-to-binary.py`, `json-combine.py` | Classic `.json` → `.bin` (some steps need ~16G RAM) |
| `utils/build-perfect-hash.py` | Combo tables → perfect-hash files for `ida_search_via_graph` |
| `utils/lookup-table-convert-to-cost-only.py` | Sparse text → cost-only |
| `lookup-tables/` | Production outputs (and copies the solver may use) |
| `tmp/` | Scratch; `make test` and every `builderui` run start empty |
| `histogram.txt` | Appended depth histograms after production saves |
| `tests/` | Unit tests + `builder_table_baselines.json` |

`make init` compiles the two C helpers + `utils/pad-lines`, creates `venv`, and installs requirements. It also `export`s `PYTHONPATH` to both this repo and the solver (that export only lasts for the make recipe; export it in your shell too).

```bash
export PYTHONPATH=/home/dwalton/rubiks-cube/rubiks-cube-NxNxN-solver:/home/dwalton/rubiks-cube/rubiks-cube-lookup-tables
make init
source venv/bin/activate
```

On the Windows workstation, use WSL Ubuntu, not native PowerShell gcc.

## Test and format

```bash
make format      # isort + black 120 + flake8 on git-known Python (honors .gitignore)
make test        # full pytest; serial; writes tables under tmp/test-lookup-tables
make test-lite   # skips test_build_* and tests/test_builder_determinism.py
```

`test_builder_tables.py` rebuilds every Makefile `builderui` class to the depth in `tests/builder_table_baselines.json` and byte-compares output. That is still a **test** build (tmp dir, tiny depths), not a production table.

If you add a `./utils/builderui.py BuildFoo` line to the Makefile, add a baseline (or an entry in `SKIPPED_BUILDERS`) or `test_every_makefile_builder_is_accounted_for` fails.

## How a table is built

```mermaid
flowchart TD
  ui["utils/builderui.py BuildXxx"] --> cls["builderNNN.py class"]
  cls --> search["builder.search depth, cores"]
  search --> crunch["builder-crunch-workq / ranked CAS mmap"]
  crunch --> save["builder.save"]
  save --> ranked["name.cost-only.bin + .json"]
  save --> graph["name.json then build-ida-graph / json-to-binary"]
  save --> hist["histogram.txt unless RUBIKS_SKIP_HISTOGRAM"]
```

1. `builderui.py` wipes `./tmp`, instantiates the class named on the command line from `builder{333…777}.py`.
2. `search(depth, cores)` BFS/IDA-expands. Ranked builders mmap a dense cost array (prefer `/dev/shm`; disk-backed mmap will thrash).
3. `save()` writes the table under `RUBIKS_LOOKUP_TABLE_DIR` or `lookup-tables/`, plus sidecar JSON for ranked files.
4. Makefile recipes then post-process: `build-ida-graph.py`, `json-to-binary.py`, `json-combine.py`, or `build-perfect-hash.py`.

`--code-gen` on `builderui.py` prints Python IDA helper classes; it does not search.

Typical **ranked** invocation (only when asked):

```bash
./utils/builderui.py Build777Phase56UDLeftMiddleObliqueCentersStage --cores 22
```

Typical **classic graph** chain (only when asked):

```bash
./utils/builderui.py Build444Reduce333LFRBCenters
./utils/build-ida-graph.py Build444Reduce333LFRBCenters
./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step31-centers.json
```

Copy or upload the solver-facing artifact (`.bin`, `.cost-only.bin`, perfect-hash) so `download_file_if_needed()` in the solver can see it. The solver wget path is the **basename** + `.gz` on S3.

## Makefile map (production)

| Make target | What it builds | Solver consumer |
| --- | --- | --- |
| `333` | MicroPython 3x3 phases | 3x3 / EV3 path |
| `444-phase12-ranked`, `444-lfrb-centers`, `444-pair-all-edges` | 4x4 ranked phase 1+2, LFRB-center graph, all-edge pairing | `ida_search_444_phase1_and_2`, `ida_search_444_phase3_and_4` |
| `555-phase1` … `555-phase6` | 5x5 prune + perfect hashes | graph IDA; phase5/6 combo hashes |
| `666-phase1` | Inner x + LR obliques, one-phase ranked | `ida_search_666_centers_stage` |
| `666-phase3-preserve-inner-x` | UD oblique / outer-x pairs | same, phase 3 |
| `666-phase5` | Three 70^5 tables: all inner-x plus one axis's obliques | `ida_search_666_daisy_centers` |
| `777-phase2` | UD inner centers ranked | `ida_search_777_centers_stage` |
| `777-phase5-6-ranked` | Six UD pairwise \(C(16,8)^2\) tables | `ida_search_777_UD_centers_stage` |
| `777-daisy-ranked` | 15 leave-one-out daisy tables | `ida_search_777_daisy_centers` |
| `777-daisy-perfect` | One symmetry-reduced 70^5 daisy table (optional) | daisy with `use_perfect_tables` |
| `777-solve-perfect` | Native-orientation twin of daisy-perfect | `--native-only` for 9x9+ |
| `777-phase5` | Older graph/perfect-hash UD obliques | leftover graph path |

`777-daisy-perfect` / `777-solve-perfect` each run a BFS over 70^5 ranks, so the
build needs that much scratch, but they publish a 314 MiB pair instead: the cost
of each orbit of the 16 axis-preserving symmetries, plus a rank-select index from
canonical raw rank to dense position. UD, LR and FB were the same cost function
in three square orderings, so one table now serves all three and the searcher
rotates onto the UD coordinate. See `center_symmetry_777.h`.

Cost **matrices** that combine per-axis table costs are **not** built here. They are C arrays in the solver, regenerated by `rubiks-cube-NxNxN-solver/utils/build-*-cost-matrix.py`.

## Ranked table formats

Sidecar `*.cost-only.bin.json` uses `dense-multiset-cost-v1` for sticker
multisets, `dense-edge-pairing-cost-v1` for the even matching between high
and low wing slots (\(n!/2\) entries; 4x4 all-edge is \(12!/2 = 239,500,800\)),
and `center-symmetry-444-cost-v1` for 24-sticker 8/8/8 centers quotiented by
the 48 cube symmetries (4x4 all-centers and 6x6 inner-x: 197,221,662 orbits).

| Field | Meaning |
| --- | --- |
| `cost_encoding` | `0` = unseen; nonzero = **depth + 1** |
| `rank_order` | left-to-right mixed radix over `rank_groups` |
| `universe_size` | mmap length in bytes (one byte per rank) |
| `states_per_depth` | histogram used by tests/docs |

Keep rank groups, square tuples, and legal moves identical to the C searcher. If you change `UFBD_*` lists in the solver, the builder class here must match.

Live ranked files during a build:

- cost array: `/dev/shm/<name>.cost-only.bin.live` if tmpfs exists, else `tmp/`
- work queue: `tmp/` (sequential, can outgrow tmpfs)

## Env vars

| Variable | Effect |
| --- | --- |
| `RUBIKS_LOOKUP_TABLE_DIR` | Where `save()` writes. Tests: `tmp/test-lookup-tables` |
| `RUBIKS_SKIP_HISTOGRAM` | Skip appending `histogram.txt` (tests set this) |
| `PYTHONPATH` | Solver + this repo |

## Adding a builde

1. Class in `builderNNN.py` (filename, moves, `rank_groups` or graph state, goal).
2. Makefile target that calls `builderui.py` and any post-process.
3. Baseline in `tests/builder_table_baselines.json` (shallow depth is fine).
4. Solver: C mmap + Python flags. Do not wire a new table into the solver until the format matches an existing searcher or you add one.
5. Run `make test-lite` plus the new baseline test. Do not kick off `--cores 22` on the real universe unless asked.

## Pitfalls

- `make clean` deletes `tmp/` and the compiled C helpers; `make init` rebuilds helpers.
- `json-to-binary.py` on large 5x5 graphs is RAM-heavy (Makefile comments ~16G).
- Histogram parse errors mean `histogram.txt` lacks your filename; tests should not touch that file.
- Sibling solver `AGENTS.md` describes which table each C binary loads. Change both sides of a flag/filename pair together.
