from src.pre_built.counter import count_ocurrences
import pytest


def test_counter():
    assert count_ocurrences("data/jobs.csv", "python") == 1639


def test_counter_2():
    assert count_ocurrences("data/jobs.csv", "javascript") == 122


def test_fail_counter():
    with pytest.raises(FileNotFoundError, match="File not found"):
        count_ocurrences("data/test_fail.csv", "a")
