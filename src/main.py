import sys
from task_manager import add_task, remove_task, update_task
from storage import read_json, write_json
from ui import display_menu, validate_users_menu_choice, display_users_tasks

FILENAME = "users_tasks.json"


def main() -> None:
    while True:
        users_tasks: list[dict] = read_json(FILENAME)
        display_users_tasks(users_tasks)
        display_menu()
        users_choice: int = validate_users_menu_choice()

        match users_choice:
            case 1:
                users_tasks = add_task(users_tasks)
            case 2:
                users_tasks = remove_task(users_tasks)
            case 3:
                users_tasks = update_task(users_tasks)
            case 4:
                print("Goodbye! :)")
                sys.exit()

        write_json(FILENAME, users_tasks)


if __name__ == "__main__":
    main()
