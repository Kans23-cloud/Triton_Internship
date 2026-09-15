# Triton Internship

## Day 2: Iterators, Generators & Memory-Efficient Data Handling

This branch contains the implementation for Day 2 of the Triton internship.

The task focuses on processing large amounts of customer data efficiently without loading the entire dataset into memory.

### Project

Customer Churn Detection

### Objective

Build a custom data-loading mechanism that:

- Reads CSV files from a folder.
- Processes records in batches.
- Uses lazy evaluation.
- Avoids storing the complete dataset in memory.
- Measures memory usage as the dataset size increases.

### Concepts Covered

- Iterators
- `__iter__()`
- `__next__()`
- Generators
- `yield`
- Lazy evaluation
- Eager evaluation
- `os.scandir()`
- `itertools`
- Memory measurement using `tracemalloc`

### Implementation

The project contains two data-loading approaches:

1. `CSVDatasetIterator`
   - A custom iterator class.
   - Implements `__iter__()` and `__next__()`.
   - Returns one batch of customer records at a time.

2. `csv_dataset_generator()`
   - A generator function.
   - Uses `yield` to pause and resume execution.
   - Reads and returns records lazily in batches.

### Memory Benchmark

The benchmark compares memory usage for datasets containing:

- 100 CSV files
- 1,000 CSV files
- 10,000 CSV files

Run the benchmark from inside the `customer_churn` folder:

```powershell
python -m scripts.memory_benchmark