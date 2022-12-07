import pytest
from src.pre_built.counter import count_ocurrences


def test_counter_python():
    assert count_ocurrences("data/jobs.csv", "python") == 1639


def test_counter_javascript():
    assert count_ocurrences("data/jobs.csv", "javascript") == 122


def test_counter_fail():
    with pytest.raises(FileNotFoundError):
        assert count_ocurrences("data/jobs.csv", "falha")
