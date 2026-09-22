from contextlib import contextmanager


class FileResource:

    def __init__(self, file_path, mode="r"):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file is not None:
            self.file.close()


@contextmanager
def managed_file(file_path, mode="r"):
    file = open(file_path, mode)

    try:
        yield file
    finally:
        file.close()