class ChurnPipelineError(Exception):
    """Base exception for the customer churn pipeline."""


class DataValidationError(ChurnPipelineError):
    """Raised when input data is invalid."""


class ConfigError(ChurnPipelineError):
    """Raised when pipeline configuration is invalid."""


class ProcessingError(ChurnPipelineError):
    """Raised when data processing fails."""


class DataLoadingError(ChurnPipelineError):
    """Raised when data loading fails."""