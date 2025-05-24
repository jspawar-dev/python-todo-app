def display_menu() -> None:
    print("-" * 20)
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. Update a task")
    print("4. Exit")


def validate_users_menu_choice() -> int:
    while True:
        try:
            choice = int(input("What would you like to do? "))

            if choice < 1 or choice > 4:
                raise ValueError

            return choice

        except ValueError:
            print("Please enter a valid option from the menu.")


def display_users_tasks(users_tasks: list[dict]) -> None:
    for i, task in enumerate(users_tasks, 1):
        if task["completed"] is True:
            print(f'{i}. {task["task"]} \u2714')
        else:
            print(f'{i}. {task["task"]} \u2718')
