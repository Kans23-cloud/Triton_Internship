from app.services.user_service import create_user, get_users
from app.services.task_service import create_task, get_tasks
from app.schemas.validation import validate_user, validate_task
from app.utils.helpers import print_message, generate_id


def main():
    user_name = "Kanthasamy"
    user_email = "kanthasamy@example.com"

    if validate_user(user_name, user_email):
        user = create_user(user_name, user_email)
        print_message(f"User created: {user}")

    task_title = "Learn Python"
    task_description = "Complete modular Python task"

    if validate_task(task_title, task_description):
        task = create_task(task_title, task_description)
        print_message(f"Task created: {task}")

    print_message("\nAll Users:")
    print(get_users())

    print_message("\nAll Tasks:")
    print(get_tasks())

    print_message(f"\nNext User ID: {generate_id(get_users())}")
    print_message(f"Next Task ID: {generate_id(get_tasks())}")


if __name__ == "__main__":
    main()