import sys


def main() -> None:
    filename = "users-tasks.txt"

    while True:
        users_tasks = display_users_tasks(filename)
        display_menu()
        menu_choice = users_menu_choice()

        match menu_choice:
            case 1:
                users_tasks = add_task(users_tasks)
            case 2:
                if users_tasks:
                    users_tasks = remove_task(users_tasks)
                else:
                    print("You have no tasks, to remove.")
            case 3:
                print("Goodbye! :)")
                sys.exit()

        update_users_tasks(filename, users_tasks)


def display_users_tasks(filename: str) -> list[str]:
    # Create the text file incase it doesn't already exist.
    open(filename, "a").close()

    with open(filename, "r") as file:
        users_tasks = []
        for line in file:
            users_tasks.append(line.strip())

        if not users_tasks:
            print("You have no tasks.")

    for i, task in enumerate(users_tasks, start=1):
        print(f"{i}. {task}")

    return users_tasks


def display_menu() -> None:
    print("---------------")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. Exit")


def add_task(users_tasks: list[str]) -> list[str]:
    new_task = str(input("Enter new task: ")).strip()
    users_tasks.append(new_task)
    return users_tasks


def remove_task(users_tasks: list[str]) -> list[str]:
    while True:
        try:
            task_to_remove = int(input("What task would you like to remove? "))

            if task_to_remove > len(users_tasks) or task_to_remove < 1:
                raise ValueError

            users_tasks.pop(task_to_remove - 1)
            return users_tasks

        except ValueError:
            print("Please enter a valid index, from your task list.")


def users_menu_choice() -> int:
    while True:
        try:
            menu_choice = int(input("What would you like to do? "))

            if menu_choice < 1 or menu_choice > 3:
                raise ValueError

            return menu_choice

        except ValueError:
            print("Please enter a valid option, from the menu above. [1-3]")


def update_users_tasks(filename: str, users_tasks: list[str]) -> None:
    with open(filename, "w") as file:
        for task in users_tasks:
            file.write(task + "\n")


if __name__ == "__main__":
    main()
