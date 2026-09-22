from .base import Step
from ..context_managers import managed_file
from ..decorators import retry


class LoadDataStep(Step):

    def run(self, data):
        return data

    @retry(max_attempts=3)
    def load_file(self, file_path):
        with managed_file(file_path) as file:
            return file.read()