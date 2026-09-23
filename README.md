## Day 7 — Structured Logging & Production Debugging

### Topics Covered

- Python `logging` module
- Loggers, handlers and formatters
- Centralized logging configuration
- Structured JSON logging
- Log levels
- Exception logging with `logger.exception()`
- Development and production logging concepts
- Replacing `print()` with structured logs

### Implemented

Created centralized logging configuration in:

```text
src/customer_churn_detection/logging_config.py

The pipeline now records:

Pipeline start and completion
Pipeline steps
Number of records processed
Step duration
Pipeline duration
Errors and complete tracebacks

Logs are written in JSON format to:

logs/pipeline.log

A sample run containing both successful and deliberately failed execution is preserved as:

logs/day7_sample_run.log
Error Logging

Pipeline failures are recorded using logger.exception(), preserving the complete traceback and the original chained exception.

Example failure information includes:

FeatureEngineeringStep
ProcessingError
Original TypeError
Validation

The pipeline was executed with:

A successful dataset
A deliberately invalid dataset

The failed run was recorded with its complete traceback.

The production pipeline uses logging instead of print().


## Step 16: Final Git check

Run:

```powershell
git status