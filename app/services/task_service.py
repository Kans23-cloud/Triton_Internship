tasks = []

def create_task(title, description):
    task = {
        "title": title,
        "description": description,
        "completed": False
    }

    tasks.append(task)
    return task

def get_tasks():
    return tasks