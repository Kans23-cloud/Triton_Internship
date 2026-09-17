from .base import Step

class ValidateDataStep(Step):
    REQUIRED_FIELDS = {
        "customer_id",
        "tenure",
        "monthly_charges",
        "churn",
    }

    def run(self, data):
        if not isinstance(data, list):
            raise TypeError("Pipeline data must be a list of records")

        for record in data:
            missing_fields = self.REQUIRED_FIELDS - record.keys()

            if missing_fields:
                raise ValueError(
                    f"Missing required fields: {sorted(missing_fields)}"
                )

        return data