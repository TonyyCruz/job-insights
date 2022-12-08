from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    try:
        with open(path, encoding="utf-8") as file:
            content = csv.DictReader(file, delimiter=",", quotechar='"')
            response = [data for data in content]
            return response
    except KeyError:
        print("Error, file reading failed")


def get_unique_job_types(path: str) -> List[str]:
    file_data = read(path)
    response = {job["job_type"] for job in file_data}
    print(response)
    return response


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    job_by_type = [
      job
      for job in jobs
      if job["job_type"] == job_type
    ]
    return job_by_type
