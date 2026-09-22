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