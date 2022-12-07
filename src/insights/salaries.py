from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    file = read(path)
    return max([
        int(job['max_salary']) for job in file if (job['max_salary']).isdigit()
        ])
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    file = read(path)
    return min([
        int(job['min_salary']) for job in file if (job['min_salary']).isdigit()
        ])
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError
    elif (
        not str(job['min_salary']).isdigit()
        or not str(job['max_salary']).isdigit()
    ):
        raise ValueError
    elif int(job['min_salary']) > int(job['max_salary']):
        raise ValueError
    elif not str(salary).lstrip('-').isdigit():
        raise ValueError
    else:
        return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])
    raise NotImplementedError


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
    raise NotImplementedError
