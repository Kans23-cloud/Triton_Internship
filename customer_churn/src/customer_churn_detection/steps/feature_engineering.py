from .base import Step

class FeatureEngineeringStep(Step):
    def run(self, data):
        for record in data:
            record["customer_value"] = (
                record["tenure"] * record["monthly_charges"]
            )

        return data