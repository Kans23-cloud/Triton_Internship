from .base import Step
from ..exceptions import ProcessingError


class FeatureEngineeringStep(Step):
    def run(self, data):
        for index, record in enumerate(data):
            try:
                record["customer_value"] = (
                    record["tenure"] * record["monthly_charges"]
                )

            except (TypeError, KeyError) as error:
                raise ProcessingError(
                    f"Feature engineering failed at record {index}: "
                    f"could not calculate customer_value because "
                    f"required numeric values are invalid"
                ) from error

        return data