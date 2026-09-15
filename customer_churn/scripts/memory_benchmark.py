from pathlib import Path
import csv
import shutil
import tracemalloc

from src.customer_churn_detection.data_iterator import CSVDatasetIterator


def create_sample_dataset(folder_path, file_count, rows_per_file):
    folder = Path(folder_path)

    if folder.exists():
        shutil.rmtree(folder)

    folder.mkdir(parents=True, exist_ok=True)

    for file_number in range(file_count):
        file_path = folder / f"customer_{file_number}.csv"

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "customer_id",
                "tenure",
                "monthly_charges",
                "churn"
            ])

            for row_number in range(rows_per_file):
                writer.writerow([
                    f"C{file_number}_{row_number}",
                    12,
                    65.5,
                    "No"
                ])


def measure_memory(folder_path, batch_size):
    tracemalloc.start()

    iterator = CSVDatasetIterator(folder_path, batch_size)

    batch_count = 0
    row_count = 0

    for batch in iterator:
        batch_count += 1
        row_count += len(batch)

    current_memory, peak_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return {
        "batches": batch_count,
        "rows": row_count,
        "peak_memory_mb": peak_memory / (1024 * 1024)
    }


def main():
    dataset_sizes = [100, 1000, 10000]

    print("Memory Benchmark")
    print("-" * 60)

    for file_count in dataset_sizes:
        create_sample_dataset(
            "data/raw/benchmark",
            file_count=file_count,
            rows_per_file=10
        )

        result = measure_memory(
            "data/raw/benchmark",
            batch_size=32
        )

        print(f"Files: {file_count}")
        print(f"Rows processed: {result['rows']}")
        print(f"Batches: {result['batches']}")
        print(f"Peak memory: {result['peak_memory_mb']:.2f} MB")
        print("-" * 60)


if __name__ == "__main__":
    main()