from {{cookiecutter.project_package}}.functions import fun_with_doctest


def test_func_with_doctest_1():
	assert fun_with_doctest(1) == 2


def test_func_with_doctest_2():
	assert fun_with_doctest(2) == 4