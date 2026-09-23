from .base import Step
from ..context_managers import managed_file
from ..decorators import retry
from ..exceptions import DataLoadingError


class LoadDataStep(Step):

    def run(self, data):
        return data

    @retry(max_attempts=3)
    def load_file(self, file_path):
        try:
            with managed_file(file_path) as file:
                return file.read()

        except OSError as error:
            raise DataLoadingError(
                f"Data loading failed at '{file_path}': "
                f"unable to open or read the file"
            ) from error