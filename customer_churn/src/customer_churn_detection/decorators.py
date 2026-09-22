import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        elapsed_time = end_time - start_time

        print(
            f"{func.__name__} executed in "
            f"{elapsed_time:.6f} seconds"
        )

        return result

    return wrapper

def retry(max_attempts):
    if not isinstance(max_attempts, int) or max_attempts < 1:
        raise ValueError("max_attempts must be a positive integer")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except Exception as error:
                    print(
                        f"{func.__name__} failed "
                        f"on attempt {attempt}/{max_attempts}: "
                        f"{error}"
                    )

                    if attempt == max_attempts:
                        raise

        return wrapper

    return decorator