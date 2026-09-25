from .base import Step


class NormalizeChargesStep(Step):

    def run(self, data):
        for record in data:
            record["monthly_charges"] = float(
                record["monthly_charges"]
            )

        return data