from src.customer_churn_detection.pipeline import Pipeline
from src.customer_churn_detection.steps.feature_engineering import (FeatureEngineeringStep,)
from src.customer_churn_detection.steps.load_data import LoadDataStep
from src.customer_churn_detection.steps.remove_missing_values import (RemoveMissingValuesStep,)
from src.customer_churn_detection.steps.validate_data import ValidateDataStep
from src.customer_churn_detection.logging_config import configure_logging

configure_logging()
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


print("Pipeline 1: Validation")
pipeline_one = Pipeline(
    [
        ValidateDataStep(),
        RemoveMissingValuesStep(),
        FeatureEngineeringStep(),
    ]
)

try:
    print(pipeline_one.run(data))
except ValueError as error:
    print(f"Pipeline 1 failed: {error}")


print("\nPipeline 2: Missing-value removal")
pipeline_two = Pipeline(
    [
        LoadDataStep(),
        RemoveMissingValuesStep(),
        FeatureEngineeringStep(),
    ]
)

print(pipeline_two.run(data))