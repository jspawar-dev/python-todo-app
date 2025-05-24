from task import Task


def add_task(users_tasks: list[dict]) -> list[dict]:
    new_task: Task = Task(str(input("Enter new task: ")).strip())
    users_tasks.append(new_task.convert_to_dict())
    return users_tasks


def remove_task(users_tasks: list[dict]) -> list[dict]:
    if not users_tasks:
        print("Your task list is empty")
        return users_tasks

    while True:
        try:
            index = int(input("What task would you like to remove? "))

            if index > len(users_tasks) or index < 1:
                raise ValueError

            users_tasks.pop(index - 1)

            return users_tasks

        except ValueError:
            print("Please enter a valid index, from your task list.")


def update_task(users_tasks: list[dict]) -> list[dict]:
    if not users_tasks:
        print("Your task list is empty")
        return users_tasks

    while True:
        try:
            index = int(input("What task would you like to update? "))

            if index > len(users_tasks) or index < 1:
                raise ValueError

            index -= 1

            if users_tasks[index]["completed"] is False:
                users_tasks[index]["completed"] = True
            else:
                users_tasks[index]["completed"] = False

            return users_tasks

        except ValueError:
            print("Please enter a valid index, from your task list.")
