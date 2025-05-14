from {{cookiecutter.project_package}}.functions import fun_with_doctest, say_hi


def test_func_with_doctest_1():
	assert fun_with_doctest(1) == 2


def test_func_with_doctest_2():
	assert fun_with_doctest(2) == 4


def test_say_hi_with_default_name(capsys):
	say_hi()
	captured = capsys.readouterr()
	assert captured.out == "Hello, world!\n"


def test_say_hi_with_custom_name(capsys):
	say_hi("John")
	captured = capsys.readouterr()
	assert captured.out == "Hello, John!\n"