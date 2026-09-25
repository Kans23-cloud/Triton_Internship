\# Day 8 Refactoring Notes



\## 1. Single Responsibility Principle



\### Change

Extracted step execution and step-specific logging from `Pipeline.run()` into `\_run\_step()`.



\### Why

`Pipeline.run()` was responsible for pipeline execution, step logging, timing, and lifecycle management.



\### Result

Each method now has a more focused responsibility.



\---



\## 2. Dependency Inversion Principle



\### Change

`Pipeline` accepts objects implementing the `Step` abstraction.



```python

def \_\_init\_\_(self, steps: list\[Step]):

