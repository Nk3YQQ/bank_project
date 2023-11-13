import os

import pytest
from _pytest.capture import CaptureFixture

from src.decorators import log


@log(filename="mylog.txt")
def my_function(x: int | float, y: int | float) -> int | float:
    return x + y


@pytest.mark.parametrize("x, y, cod", [(1, 2, "ok"), (3, 4, "ok"), ("1", 2, "error"), ("3", 4, "error")])
def test_log_with_filename(x: int | str, y: int, cod: str) -> None:
    if os.path.exists("data/mylog.txt"):
        os.remove("data/mylog.txt")

    my_function(x, y)

    assert os.path.exists("data/mylog.txt")

    with open("data/mylog.txt", "r", encoding="utf-8") as file:
        status = file.read()

    assert cod in status


@log()
def my_other_function(x: int | float, y: int | float) -> int | float:
    return x - y


@pytest.mark.parametrize("x, y, cod", [(4, 1, "ok"), (3, 2, "ok"), ("4", 1, "error"), ("3", 2, "error")])
def test_log_without_filename(capsys: CaptureFixture[str], x: int | str, y: int | str, cod: str) -> None:
    my_other_function(x, y)
    captured = capsys.readouterr()

    assert cod in captured.out
