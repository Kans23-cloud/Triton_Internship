# Customer Churn Detection

## Day 4 - Type Hints & Pydantic Configuration

### Objective

Build a validated configuration system using Python type hints, Enums, and Pydantic.

### What Was Implemented

- Added Python type hints for configuration fields.
- Added `Enum` for `mode` and `device`.
- Added Pydantic `BaseModel` for configuration validation.
- Added strict validation for integer and float values.
- Added validation for:
  - Positive batch size
  - Threshold between 0 and 1
  - Non-empty feature columns
  - Existing data file path
  - Required fields
  - Valid mode values
  - Valid device values
  - Incorrect data types
- Added a default threshold value of `0.5`.
- Added demonstration scripts for valid and invalid configurations.
- Added automated pytest tests.

### Configuration Example

```python
ChurnConfig(
    data_path="data/raw/customers.csv",
    batch_size=32,
    feature_columns=[
        "tenure",
        "monthly_charges",
        "customer_value",
    ],
    mode="train",
    device="cpu",
    threshold=0.5,
)