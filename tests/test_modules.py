from app.services.user_service import create_user, get_users
from app.services.task_service import create_task, get_tasks
from app.schemas.validation import validate_user, validate_task
from app.utils.helpers import generate_id


def test_create_user():
    user = create_user("Test User", "test@example.com")

    assert user["name"] == "Test User"
    assert user["email"] == "test@example.com"


def test_get_users():
    users = get_users()

    assert isinstance(users, list)


def test_create_task():
    task = create_task("Test Task", "Test task description")

    assert task["title"] == "Test Task"
    assert task["description"] == "Test task description"
    assert task["completed"] is False


def test_get_tasks():
    tasks = get_tasks()

    assert isinstance(tasks, list)


def test_valid_user():
    assert validate_user("Kanthasamy", "kanthasamy@example.com") is True


def test_invalid_user():
    assert validate_user("", "") is False


def test_valid_task():
    assert validate_task("Learn Python", "Complete internship task") is True


def test_invalid_task():
    assert validate_task("", "") is False


def test_generate_id():
    items = ["item1", "item2"]

    assert generate_id(items) == 3