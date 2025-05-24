import json


def read_json(filename: str) -> list[dict]:
    # Create the file, if it doesn't exist already.
    open(filename, "a").close()

    with open(filename, "r") as file:
        users_tasks = file.read().strip()
        if users_tasks:
            return json.loads(users_tasks)
        else:
            return []


def write_json(filename: str, users_tasks: list[dict]) -> None:
    with open(filename, "w") as file:
        json.dump(users_tasks, file, indent=2)
