# A Cookiecutter Template for Simple Python Projects

This is a template to generate simple Python projects that can be packaged and
installed with setuptools.

I've tried to keep the configuration simple and understandable while including
enough features to make the projects usable out of the box:

- Generate a locally installable package
- Configure pytest to run the project tests and doctests
- Configure tox to run test the projects with several Python versions

By default the generated project uses conda to create virtual environments for
tox, but that can easily be changed in `tox.ini`.

## Usage

Run

```shell script
$ cookiecutter https://github.com/hoelzl/trivial_python_project
```

Answer the questions about the project configuration and enjoy your awesome new
project.
