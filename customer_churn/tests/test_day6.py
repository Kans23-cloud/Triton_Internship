import pytest

from src.customer_churn_detection.exceptions import (
    ChurnPipelineError,
    DataLoadingError,
    DataValidationError,
    ProcessingError,
)
from src.customer_churn_detection.steps.feature_engineering import (
    FeatureEngineeringStep,
)
from src.customer_churn_detection.steps.load_data import LoadDataStep
from src.customer_churn_detection.steps.validate_data import ValidateDataStep


def test_validation_error():
    with pytest.raises(DataValidationError):
        ValidateDataStep().run([
            {
                "customer_id": "C001",
                "tenure": 12,
            }
        ])


def test_processing_error():
    with pytest.raises(ProcessingError) as error:
        FeatureEngineeringStep().run([
            {
                "customer_id": "C001",
                "tenure": "twelve",
                "monthly_charges": 65.5,
                "churn": "No",
            }
        ])

    assert isinstance(error.value, ChurnPipelineError)
    assert error.value.__cause__ is not None
    assert isinstance(error.value.__cause__, TypeError)


def test_loading_error():
    with pytest.raises(DataLoadingError) as error:
        LoadDataStep().load_file("data/raw/missing.csv")

    assert isinstance(error.value, ChurnPipelineError)
    assert error.value.__cause__ is not None


def test_exception_hierarchy():
    assert issubclass(DataValidationError, ChurnPipelineError)
    assert issubclass(DataLoadingError, ChurnPipelineError)
    assert issubclass(ProcessingError, ChurnPipelineError)