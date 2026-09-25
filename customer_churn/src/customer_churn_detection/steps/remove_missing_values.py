from .base import Step


class RemoveMissingValuesStep(Step):
    def run(self, data):
        return [
            record
            for record in data
            if all(value is not None for value in record.values())
        ]