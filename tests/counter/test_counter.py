from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("tests/mocks/jobs.csv", "back") == 1
    assert count_ocurrences("tests/mocks/jobs.csv", "dkt") == 0
    assert count_ocurrences("tests/mocks/jobs.csv", "time") == 2
    assert count_ocurrences("tests/mocks/jobs.csv", "000") == 3
    assert count_ocurrences("tests/mocks/jobs.csv", "t") == 8
