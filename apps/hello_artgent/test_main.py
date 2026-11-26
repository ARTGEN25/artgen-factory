import pytest

from apps.hello_artgent.main import get_greeting, main


def test_get_greeting_default():
    assert get_greeting() == "Hello Artgent"


def test_get_greeting_trims_whitespace():
    assert get_greeting(" Artgent ") == "Hello Artgent"
    assert get_greeting("\tAda\n") == "Hello Ada"


@pytest.mark.parametrize("bad_name", ["", " ", 123, None])
def test_get_greeting_rejects_empty_and_non_string(bad_name):
    with pytest.raises(ValueError):
        get_greeting(bad_name)


def test_main_default_prints_greeting(capsys):
    assert main([]) == 0
    captured = capsys.readouterr()
    assert captured.out == "Hello Artgent\n"
    assert captured.err == ""


def test_main_name_option(capsys):
    assert main(["--name", " Ada "]) == 0
    captured = capsys.readouterr()
    assert captured.out == "Hello Ada\n"
    assert captured.err == ""


def test_main_whitespace_name_fails_cleanly(capsys):
    assert main(["--name", " "]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "error:" in captured.err
