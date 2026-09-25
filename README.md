## Day 8 — Clean Code & SOLID Refactoring

### Objective

Refactor the existing customer churn pipeline using clean code principles and SOLID design principles without changing its core behavior.

### Concepts Covered

- Single Responsibility Principle (SRP)
- Open/Closed Principle (OCP)
- Dependency Inversion Principle (DIP)
- DRY
- Meaningful naming
- Extract function refactoring
- Step-based pipeline design

### Refactoring Performed

#### 1. Single Responsibility Principle

The pipeline previously handled pipeline execution, step execution, step logging, and timing inside `run()`.

The step execution logic was extracted into:

```python
_run_step()

This makes Pipeline.run() responsible for pipeline-level execution while _run_step() handles individual step execution and logging.

2. Dependency Inversion Principle

The pipeline now works with the abstract Step class:

class Step(ABC):
    @abstractmethod
    def run(self, data):
        pass

Pipeline depends on the Step abstraction rather than specific preprocessing implementations.

This allows different processing steps to be supplied without modifying the pipeline.

3. Open/Closed Principle

Added:

NormalizeChargesStep

without modifying the core pipeline implementation.

A new preprocessing step can now be created by implementing the Step abstraction and adding it to the pipeline.

4. DRY

Common step execution logic such as:

Step timing
Step start logging
Step completion logging
Step execution

was centralized inside _run_step() instead of being duplicated.

5. Meaningful Naming

Improved naming was used throughout the refactored code, including:

NormalizeChargesStep
_run_step
step_name
duration

These names make the purpose of each component clear.

New Files
REFACTOR_NOTES.md
src/customer_churn_detection/steps/normalize_charges.py
tests/test_day8.py
Modified Files
src/customer_churn_detection/pipeline.py
scripts/demo_pipeline.py
Validation

The complete test suite was executed after the refactoring.

The new Day 8 tests verify:

Pipeline steps follow the Step abstraction.
Monthly charges are normalized correctly.
A new preprocessing step can be added without modifying Pipeline.
Result

The pipeline now follows a modular step-based architecture.

New preprocessing functionality can be introduced by creating a new Step implementation without changing the core pipeline execution logic.

Detailed refactoring decisions are documented in:

REFACTOR_NOTES.md

After adding it, run:

```powershell
python -m pytest -q