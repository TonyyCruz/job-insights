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
        print('Invalid params')
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filtered_jobs = [
      job
      for job in jobs
      if matches_salary_range(job, salary)
    ]
    return filtered_jobs
