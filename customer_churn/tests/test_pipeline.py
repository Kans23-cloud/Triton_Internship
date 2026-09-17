from src.customer_churn_detection.pipeline import Pipeline
from src.customer_churn_detection.steps.feature_engineering import (FeatureEngineeringStep,)
from src.customer_churn_detection.steps.load_data import LoadDataStep
from src.customer_churn_detection.steps.validate_data import ValidateDataStep
from src.customer_churn_detection.steps.remove_missing_values import (RemoveMissingValuesStep,)

def test_pipeline_runs_steps_in_sequence():
    data = [
        {
            "customer_id": "C001",
            "tenure": 12,
            "monthly_charges": 65.5,
            "churn": "No",
        }
    ]

    pipeline = Pipeline(
        [
            LoadDataStep(),
            ValidateDataStep(),
            FeatureEngineeringStep(),
        ]
    )

    result = pipeline.run(data)

    assert result[0]["customer_value"] == 786.0

def test_pipeline_can_swap_steps_without_editing_pipeline():
    data = [
        {
            "customer_id": "C001",
            "tenure": 12,
            "monthly_charges": 65.5,
            "churn": "No",
        },
        {
            "customer_id": "C002",
            "tenure": None,
            "monthly_charges": 70.0,
            "churn": "Yes",
        },
    ]

    pipeline = Pipeline(
        [
            LoadDataStep(),
            RemoveMissingValuesStep(),
            FeatureEngineeringStep(),
        ]
    )

    result = pipeline.run(data)

    assert len(result) == 1
    assert result[0]["customer_id"] == "C001"
    assert result[0]["customer_value"] == 786.0