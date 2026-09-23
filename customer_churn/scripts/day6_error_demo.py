from src.customer_churn_detection.exceptions import (
    ChurnPipelineError,
)
from src.customer_churn_detection.steps.feature_engineering import (
    FeatureEngineeringStep,
)
from src.customer_churn_detection.steps.load_data import LoadDataStep
from src.customer_churn_detection.steps.validate_data import ValidateDataStep


def run_demo(name, function):
    print(f"\n--- {name} ---")

    try:
        function()

    except ChurnPipelineError as error:
        print(f"Pipeline error: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")


def validation_failure():
    ValidateDataStep().run([
        {
            "customer_id": "C001",
            "tenure": 12,
        }
    ])


def processing_failure():
    FeatureEngineeringStep().run([
        {
            "customer_id": "C001",
            "tenure": "twelve",
            "monthly_charges": 65.5,
            "churn": "No",
        }
    ])


def loading_failure():
    LoadDataStep().load_file("data/raw/missing.csv")


run_demo("Data validation failure", validation_failure)
run_demo("Processing failure", processing_failure)
run_demo("Data loading failure", loading_failure)