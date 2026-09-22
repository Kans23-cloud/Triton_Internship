## Day 5 — Decorators, Context Managers & Caching

### Topics Covered

- Custom decorators
- `functools.wraps`
- Decorators with arguments
- Retry logic
- Context managers
- `__enter__` and `__exit__`
- `contextlib.contextmanager`
- `functools.lru_cache`
- Cache hits and misses
- Risks of mutable cached results and unbounded caching

### Implemented

#### 1. `@timeit`

Measures and prints the execution time of a function.

Applied to:

```python
Pipeline.run()

2. @retry(max_attempts=N)

Automatically retries a function when it raises an exception.

Applied to:

LoadDataStep.load_file()
3. managed_file

A context manager that safely opens and closes files, including when an exception occurs.

Used by:

LoadDataStep.load_file()
4. lru_cache

Demonstrated caching using:

@lru_cache(maxsize=3)

Repeated calls with the same arguments are served from the cache instead of executing the function again.

Validation

All Day 5 tests passed successfully.

The caching demonstration produced:

CacheInfo(hits=1, misses=2, maxsize=3, currsize=2)

This confirms that repeated function calls can be served from the cache.

Files Added
src/customer_churn_detection/decorators.py
src/customer_churn_detection/context_managers.py
tests/test_day5.py
scripts/demo_cache.py
Files Updated
src/customer_churn_detection/pipeline.py
src/customer_churn_detection/steps/load_data.py

After saving, run:

```powershell
python -m pytest -q