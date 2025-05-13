# {{cookiecutter.project_name}}

{{cookiecutter.description}}


## Installation using setuptools

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

## Working with the project using setuptools

The project is configured to run `pytest` tests and doctests. Source code for
tests is in the `tests` directory, outside the main package directory. Therefore,
you have to make sure that your python interpreter can resolve the imports for
the tests. The easiest way to ensure this is to install the package. You can run
the tests from the root directory as follows:

```shell script
$ pytest
```

*Note:* If you install the package from a wheel, the tests will run against the
installed package; install in editable mode (i.e., using the `-e` option) to
test against the development package.

To check that the package works correctly with different Python versions by executing

```shell script
$ tox
```

from the project's root directory. Currently, Python versions 3.8 to 3.11
are tested. Dependencies for `tox` are installed using `tox-conda`; remove the
corresponding entry in the `tox.ini` file if you want to use `virtualenv`
instead.

## Working with the project using uv

To build the project, use

```shell script
uv build
```

To run the executable, use

```shell script
uv run python -m {{cookiecutter.project_package}}
```

To run the tests, use

```shell script
uv run pytest
```

To run tox, use

```shell script
uv run tox
```
