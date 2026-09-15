from pathlib import Path
import csv
import os

class CSVDatasetIterator:
    def __init__(self, folder_path, batch_size):
        self.folder_path = Path(folder_path)
        self.batch_size = batch_size
        self.files = (
            entry
            for entry in os.scandir(self.folder_path)
            if entry.is_file() and entry.name.endswith(".csv")
        )
        self.current_file = None
        self.current_reader = None

    def __iter__(self):
        return self

    def __next__(self):
        batch = []

        while len(batch) < self.batch_size:
            if self.current_reader is None:
                try:
                    file_entry=next(self.files)
                except StopIteration:
                    break

                self.current_file = open(
                    file_entry.path,
                    "r",
                    newline="",
                    encoding="utf-8"
                )

                self.current_reader = csv.DictReader(self.current_file)

            try:
                row = next(self.current_reader)
                batch.append(row)

            except StopIteration:
                self.current_file.close()
                self.current_file = None
                self.current_reader = None

        if not batch:
            raise StopIteration

        return batch

def csv_dataset_generator(folder_path, batch_size):
    folder = Path(folder_path)
    files = sorted(folder.glob("*.csv"))
    batch = []

    for file_path in files:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                batch.append(row)

                if len(batch) == batch_size:
                    yield batch
                    batch = []

    if batch:
        yield batch