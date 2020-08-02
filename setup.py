from setuptools import find_packages, setup

with open("README.md") as fh:
    readme_text = fh.read()

with open("LICENSE") as fh:
    license_text = fh.read()

setup(
    name="rubikscubelookuptables",
    version="1.0.0",
    description="rubiks cube NxNxN lookup tables builder",
    long_description=readme_text,
    url="https://github.com/dwalton76/rubiks-cube-lookup-tables",
    author="Daniel Walton",
    author_email="dwalton76@gmail.com",
    license=license_text,
    packages=["rubikscubelookuptables"],
)
