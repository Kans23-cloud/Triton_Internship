from src.customer_churn_detection.data_iterator import (
    CSVDatasetIterator,
    csv_dataset_generator,
)


def create_test_csv(folder, file_name, row_count):
    file_path = folder / file_name

    content = "customer_id,churn\n"

    for row_number in range(row_count):
        content += f"C{row_number},No\n"

    file_path.write_text(content, encoding="utf-8")


def test_iterator_returns_batches(tmp_path):
    create_test_csv(tmp_path, "customers.csv", 5)

    iterator = CSVDatasetIterator(tmp_path, 2)

    batches = list(iterator)

    assert [len(batch) for batch in batches] == [2, 2, 1]
    assert sum(len(batch) for batch in batches) == 5


def test_generator_returns_batches(tmp_path):
    create_test_csv(tmp_path, "customers.csv", 5)

    batches = list(csv_dataset_generator(tmp_path, 2))

    assert [len(batch) for batch in batches] == [2, 2, 1]
    assert sum(len(batch) for batch in batches) == 5