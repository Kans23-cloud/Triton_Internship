from src.customer_churn_detection.pipeline import Pipeline
from src.customer_churn_detection.steps.base import Step
from src.customer_churn_detection.steps.normalize_charges import (
    NormalizeChargesStep,
)


def test_pipeline_accepts_step_abstraction():
    step = NormalizeChargesStep()

    assert isinstance(step, Step)


def test_normalize_charges():
    data = [
        {
            "customer_id": "C001",
            "tenure": 12,
            "monthly_charges": "65.5",
            "churn": "No",
        }
    ]

    result = NormalizeChargesStep().run(data)

    assert result[0]["monthly_charges"] == 65.5


def test_new_step_can_be_added_without_pipeline_changes():
    pipeline = Pipeline(
        [
            NormalizeChargesStep(),
        ]
    )

    data = [
        {
            "customer_id": "C001",
            "tenure": 12,
            "monthly_charges": "65.5",
            "churn": "No",
        }
    ]

    result = pipeline.run(data)

    assert result[0]["monthly_charges"] == 65.5