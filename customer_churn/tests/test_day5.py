import pytest

from src.customer_churn_detection.context_managers import managed_file
from src.customer_churn_detection.decorators import retry, timeit


def test_timeit_preserves_function_metadata():
    @timeit
    def sample_function():
        return "done"

    assert sample_function() == "done"
    assert sample_function.__name__ == "sample_function"


def test_retry_succeeds_after_failures():
    attempts = 0

    @retry(max_attempts=3)
    def unstable_function():
        nonlocal attempts
        attempts += 1

        if attempts < 3:
            raise ValueError("Temporary failure")

        return "success"

    assert unstable_function() == "success"
    assert attempts == 3


def test_retry_raises_after_max_attempts():
    attempts = 0

    @retry(max_attempts=3)
    def failing_function():
        nonlocal attempts
        attempts += 1
        raise ValueError("Permanent failure")

    with pytest.raises(ValueError):
        failing_function()

    assert attempts == 3


def test_retry_rejects_invalid_attempt_count():
    with pytest.raises(ValueError):
        retry(max_attempts=0)


def test_managed_file_closes_resource():
    file_path = "data/raw/customers.csv"

    with managed_file(file_path) as file:
        assert not file.closed

    assert file.closed


def test_managed_file_closes_after_exception():
    file_path = "data/raw/customers.csv"

    with pytest.raises(ValueError):
        with managed_file(file_path) as file:
            assert not file.closed
            raise ValueError("Something went wrong")

    assert file.closed