from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    jobs_data = read(path)
    max_salaries = max(
      int(job["max_salary"])
      for job in jobs_data
      if job["max_salary"]
      and job["max_salary"].isdigit()
    )
    return max_salaries


def get_min_salary(path: str) -> int:
    jobs_data = read(path)
    min_salary = min(
        int(job["min_salary"])
        for job in jobs_data
        if job["min_salary"]
        and job["min_salary"].isdigit()
    )
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if int(job["max_salary"]) < int(job["min_salary"]):
            raise ValueError(
                "Parameter data does not exist or has an invalid format"
            )

        return int(job["max_salary"]) >= int(salary) >= int(job["min_salary"])
    except (ValueError, KeyError, TypeError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:

    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            continue

    return filtered_jobs
