def get_tasks():
    return [
        {"name": "easy", "rows": 4, "cols": 4, "cliffs": []},
        {"name": "medium", "rows": 4, "cols": 12, "cliffs": [(3, i) for i in range(1, 11)]},
        {"name": "hard", "rows": 6, "cols": 12, "cliffs": [(5, i) for i in range(1, 11)]}
    ]
