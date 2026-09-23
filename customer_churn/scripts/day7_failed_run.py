import logging

from src.customer_churn_detection.logging_config import configure_logging
from src.customer_churn_detection.pipeline import Pipeline
from src.customer_churn_detection.steps.feature_engineering import FeatureEngineeringStep
from src.customer_churn_detection.steps.validate_data import ValidateDataStep


configure_logging()

logger = logging.getLogger(__name__)


data = [
    {
        "customer_id": "C001",
        "tenure": "invalid",
        "monthly_charges": 65.5,
        "churn": "No",
    }
]

pipeline = Pipeline(
    [
        ValidateDataStep(),
        FeatureEngineeringStep(),
    ]
)

try:
    pipeline.run(data)

except Exception:
    logger.exception(
        "Deliberately failed pipeline run",
        extra={
            "event": "intentional_failure",
        },
    )