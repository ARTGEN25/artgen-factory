import pytest

from apps.hello_artgent.main import get_greeting, main


def test_get_greeting_default():
    assert get_greeting() == "Hello Artgent"
    assert get_greeting(None) == "Hello Artgent"


def test_get_greeting_trims_whitespace():
    assert get_greeting("  Ada  ") == "Hello Ada"
    assert get_greeting("\tGrace\n") == "Hello Grace"


def test_get_greeting_rejects_empty_and_invalid():
    with pytest.raises(ValueError):
        get_greeting("")
    with pytest.raises(ValueError):
        get_greeting("   ")

    with pytest.raises(TypeError):
        get_greeting(42)


def test_cli_default_output(capsys):
    assert main([]) == 0
    captured = capsys.readouterr()
    assert captured.out == "Hello Artgent\n"
    assert captured.err == ""


def test_cli_name_output(capsys):
    assert main(["Ada"]) == 0
    captured = capsys.readouterr()
    assert captured.out == "Hello Ada\n"
    assert captured.err == ""


def test_cli_trims_whitespace(capsys):
    assert main(["  Ada  "]) == 0
    captured = capsys.readouterr()
    assert captured.out == "Hello Ada\n"


def test_cli_empty_name_exits_2(capsys):
    with pytest.raises(SystemExit) as excinfo:
        main(["   "])
    assert excinfo.value.code == 2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "name must not be empty" in captured.err


def test_cli_invalid_args_exits_2(capsys):
    with pytest.raises(SystemExit) as excinfo:
        main(["Ada", "Grace"])
    assert excinfo.value.code == 2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "usage:" in captured.err.lower()
