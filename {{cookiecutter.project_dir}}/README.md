# Package {{cookiecutter.project_package}}

{{cookiecutter.description}}


## Installation

To build the project use

```shell script
python -m build
```
in the root directory (i.e., the directory where `pyproject.toml` and
`setup.cfg` live).

After building the package you can install it with pip:
```shell script
pip install dist/{{cookiecutter.project_package}}-0.0.1-py3-none-any.whl
```

To install the package so that it can be used for development purposes
install it with
```shell script
pip install -e .
```
in the root directory.

## Working with the project

The project is configured to run `pytest` tests. Tests are in the `tests`
directory, outside the main package directory.  Therefore you have to install
the package before running the tests. Once the package is installed, enter
`pytest` in the root of the project to run the tests.

*Note:* If you install the package from a wheel, the tests will run against the
installed package; install in editable mode (i.e., using the `-e` option) to
test against the development package.

To check that the package works correctly with different Python versions using
`tox`. Currently versions 3.8, 3.9 and 3.10 are tested. Dependencies for `tox`
are installed using `tox-conda`; remove the corresponding entry in the `tox.ini`
file if you want to use `virtualenv` instead.

