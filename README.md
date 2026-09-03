# Task Management API

A modular Python project demonstrating production-style code organization
using separate modules for user management, task management, validation,
and utility functions.

## Project Objective

The objective of this project is to demonstrate how Python applications
can be organized into multiple modules instead of placing all functionality
inside a single Python file.

## Features

- User management
- Task management
- Input validation
- Reusable utility functions
- Modular project structure
- Automated testing using pytest

## Project Structure

```text
task-management-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   │
│   ├── models/
│   │   └── __init__.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── validation.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── task_service.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── tests/
│   ├── __init__.py
|   └── test_modules.py
│
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

## Module Responsibilities

### User Management

**File:** `app/services/user_service.py`

Responsible for user-related operations such as:

- Creating users
- Retrieving users

### Task Management

**File:** `app/services/task_service.py`

Responsible for task-related operations such as:

- Creating tasks
- Retrieving tasks

### Validation

**File:** `app/schemas/validation.py`

Contains validation functions for:

- User data
- Task data

### Utility Functions

**File:** `app/utils/helpers.py`

Contains reusable utility functions such as:

- Printing messages
- Generating IDs

### Main Application

**File:** `app/main.py`

Acts as the entry point of the application and coordinates the different
modules.

## Testing

The project uses pytest for automated testing.

Run the tests using:

```bash
pytest
