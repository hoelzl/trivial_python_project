# A Cookiecutter Template for Simple Python Projects

This is a template to generate simple Python projects that can be packaged and
installed with setuptools and/or uv.

I've tried to keep the configuration simple and understandable while including
enough features to make the projects usable out of the box:

- Generate a locally installable package
- Configure pytest to run the project tests and doctests
- Configure tox to test the projects with several Python versions
- Configure bumpversion to manage project versions

Bumpversion is configured to *not* commit the updated files. This is the safer
option but slightly inconvenient. To enable automatic commits, change
`commit = False` to `commit = True` in `.bumpversion.cfg`.

## Usage

Run

```shell script
$ cookiecutter https://github.com/hoelzl/trivial_python_project
```

Answer the questions about the project configuration and enjoy your awesome new
project.
