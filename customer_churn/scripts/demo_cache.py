import time
from functools import lru_cache


@lru_cache(maxsize=3)
def expensive_calculation(number):
    print(f"Calculating for {number}...")

    time.sleep(1)

    return number * number


print("First call:")
print(expensive_calculation(10))

print("\nSecond call with same input:")
print(expensive_calculation(10))

print("\nDifferent input:")
print(expensive_calculation(20))

print("\nCache information:")
print(expensive_calculation.cache_info())