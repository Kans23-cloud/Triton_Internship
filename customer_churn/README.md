# Customer Churn Detection

A machine learning project foundation for customer churn detection.

## Setup

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -e .
```

## Project Structure

- `src/` - Source code
- `data/` - Dataset files
- `notebooks/` - Jupyter notebooks
- `configs/` - Configuration files
- `scripts/` - Utility scripts
- `tests/` - Test files
- `models/` - Model files

## Status

Project environment and repository foundation completed.

## Day 2: Iterators, Generators, and Memory-Efficient Data Handling

The project includes a custom CSV iterator and generator for processing customer data in batches.

Instead of loading all CSV files and records into memory at once, the implementation reads files lazily and returns one batch at a time.

### Concepts Used

- `__iter__()` and `__next__()` for building a custom iterator.
- `yield` for creating a generator.
- Lazy evaluation for processing data only when requested.
- `os.scandir()` for efficient file iteration.
- `csv.DictReader` for reading CSV records.
- `tracemalloc` for measuring memory usage.

### Run the Memory Benchmark

From the `customer_churn` folder, run:

```powershell
python -m scripts.memory_benchmark