from .base import Step
from ..exceptions import DataValidationError


class ValidateDataStep(Step):
    REQUIRED_FIELDS = {
        "customer_id",
        "tenure",
        "monthly_charges",
        "churn",
    }

    def run(self, data):
        if not isinstance(data, list):
            raise DataValidationError(
                "Data validation failed at ValidateDataStep: "
                "expected a list of customer records"
            )

        for index, record in enumerate(data):
            if not isinstance(record, dict):
                raise DataValidationError(
                    f"Data validation failed at record {index}: "
                    f"expected a dictionary, got {type(record).__name__}"
                )

            missing_fields = self.REQUIRED_FIELDS - record.keys()

            if missing_fields:
                raise DataValidationError(
                    f"Data validation failed at record {index}: "
                    f"missing required fields {sorted(missing_fields)}"
                )

        return data