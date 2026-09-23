## Day 6 — Exception Hierarchies & Error Design

### Topics Covered

- Python exception hierarchy
- Custom exception classes
- Exception chaining with `raise ... from`
- `try`, `except`, `else`, and `finally`
- Specific exception handling
- Error propagation between layers
- Why broad `except Exception` should be avoided

### Implemented

Created a project-specific exception hierarchy:

```text
ChurnPipelineError
├── DataValidationError
├── ConfigError
├── ProcessingError
└── DataLoadingError
Pipeline Error Handling
ValidateDataStep raises DataValidationError
FeatureEngineeringStep raises ProcessingError
LoadDataStep raises DataLoadingError
Low-level errors are preserved using exception chaining
Top-level code catches ChurnPipelineError and reports the failure

Example:

raise ProcessingError(
    "Feature engineering failed at record 0: "
    "could not calculate customer_value because "
    "required numeric values are invalid"
) from error

This preserves the original exception while providing a meaningful application-level error.

Validation

Day 6 tests:

21 passed

Failure scenarios were tested for:

Data validation
Data processing
Data loading
Exception hierarchy
Exception chaining

---

## Step 9: Check everything

Run:

```powershell
git status