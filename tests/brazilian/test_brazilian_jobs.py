from src.pre_built.brazilian_jobs import read_brazilian_file
import pytest


def test_brazilian_jobs():
    assert read_brazilian_file("tests/mocks/brazilians_jobs.csv")[0] == {
        'title': 'Maquinista', 'salary': '2000', 'type': 'trainee'
    }


def test_brazilian_jobs_fail():
    with pytest.raises(FileNotFoundError, match="File not found"):
        read_brazilian_file("tests/mocks/test_fail.csv")
