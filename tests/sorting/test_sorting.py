from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "title": "Software Engineer",
            "company": "Google",
            "min_salary": 100000,
            "max_salary": 200000,
            "date_posted": "2021-01-01",
        },
        {
            "title": "Software Engineer",
            "company": "Google",
            "min_salary": 100000,
            "max_salary": 200000,
            "date_posted": "2021-01-02",
        },
        {
            "title": "Software Engineer",
            "company": "Google",
            "min_salary": 100000,
            "max_salary": 200000,
            "date_posted": "2021-01-03",
        },
    ]
    sort_by(jobs, "date_posted")
    assert jobs == [
        {
            "title": "Software Engineer",
            "company": "Google",
            "min_salary": 100000,
            "max_salary": 200000,
            "date_posted": "2021-01-03",
        },
        {
            "title": "Software Engineer",
            "company": "Google",
            "min_salary": 100000,
            "max_salary": 200000,
            "date_posted": "2021-01-02",
        },
        {
            "title": "Software Engineer",
            "company": "Google",
            "min_salary": 100000,
            "max_salary": 200000,
            "date_posted": "2021-01-01",
        },
    ]


def test_sort_by_criteria_2():
    jobs = [
        {
            "title": "Software Engineer",
            "company": "Google",
            "min_salary": 300000,
            "max_salary": 400000,
            "date_posted": "2021-01-01",
        },
        {
            "title": "Software Engineer",
            "company": "Google",
            "min_salary": 200000,
            "max_salary": 300000,
            "date_posted": "2021-01-02",
        },
        {
            "title": "Software Engineer",
            "company": "Google",
            "min_salary": 100000,
            "max_salary": 200000,
            "date_posted": "2021-01-03",
        },
    ]
    sort_by(jobs, "min_salary")
    assert jobs == [
        {
            "title": "Software Engineer",
            "company": "Google",
            "min_salary": 100000,
            "max_salary": 200000,
            "date_posted": "2021-01-03",
        },
        {
            "title": "Software Engineer",
            "company": "Google",
            "min_salary": 200000,
            "max_salary": 300000,
            "date_posted": "2021-01-02",
        },
        {
            "title": "Software Engineer",
            "company": "Google",
            "min_salary": 300000,
            "max_salary": 400000,
            "date_posted": "2021-01-01",
        },
    ]
