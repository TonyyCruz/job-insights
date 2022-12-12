from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture
def jobs_mock():
    return [{
      "id": 1,
      "min_salary": "3000",
      "max_salary": "7000",
      "date_posted": "2022-11-02"
    }, {
      "id": 2,
      "min_salary": "2100",
      "max_salary": "4250",
      "date_posted": "2022-02-08"
    }, {
      "id": 3,
      "min_salary": "3200",
      "max_salary": "10000",
      "date_posted": "2022-10-11"
    }
    ]


min_order = [
    {
      "id": 2,
      "min_salary": "2100",
      "max_salary": "4250",
      "date_posted": "2022-02-08"
    }, {
      "id": 1,
      "min_salary": "3000",
      "max_salary": "7000",
      "date_posted": "2022-11-02"
    }, {
      "id": 3,
      "min_salary": "3200",
      "max_salary": "10000",
      "date_posted": "2022-10-11"
    }
    ]

max_order = [
    {
      "id": 3,
      "min_salary": "3200",
      "max_salary": "10000",
      "date_posted": "2022-10-11"
    }, {
      "id": 1,
      "min_salary": "3000",
      "max_salary": "7000",
      "date_posted": "2022-11-02"
    }, {
      "id": 2,
      "min_salary": "2100",
      "max_salary": "4250",
      "date_posted": "2022-02-08"
    }
    ]

data_order = [
    {
      "id": 1,
      "min_salary": "3000",
      "max_salary": "7000",
      "date_posted": "2022-11-02"
    }, {
      "id": 3,
      "min_salary": "3200",
      "max_salary": "10000",
      "date_posted": "2022-10-11"
    }, {
      "id": 2,
      "min_salary": "2100",
      "max_salary": "4250",
      "date_posted": "2022-02-08"
    }
    ]


def test_sort_by_criteria(jobs_mock):
    sort_by(jobs_mock, "min_salary")
    assert jobs_mock == min_order

    sort_by(jobs_mock, "max_salary")
    assert jobs_mock == max_order

    sort_by(jobs_mock, "date_posted")
    assert jobs_mock == data_order
