import pytest
from pydantic import ValidationError

from configs.config import ChurnConfig


VALID_CONFIG = {
    "data_path": "data/raw/customers.csv",
    "batch_size": 32,
    "feature_columns": [
        "tenure",
        "monthly_charges",
        "customer_value",
    ],
    "mode": "train",
    "device": "cpu",
    "threshold": 0.5,
}


def test_valid_config():
    config = ChurnConfig(**VALID_CONFIG)

    assert config.batch_size == 32
    assert config.threshold == 0.5
    assert config.mode.value == "train"
    assert config.device.value == "cpu"


def test_invalid_batch_size():
    config_data = VALID_CONFIG.copy()
    config_data["batch_size"] = -10

    with pytest.raises(ValidationError):
        ChurnConfig(**config_data)


def test_invalid_threshold():
    config_data = VALID_CONFIG.copy()
    config_data["threshold"] = 1.5

    with pytest.raises(ValidationError):
        ChurnConfig(**config_data)


def test_invalid_data_path():
    config_data = VALID_CONFIG.copy()
    config_data["data_path"] = "data/raw/does_not_exist.csv"

    with pytest.raises(ValidationError):
        ChurnConfig(**config_data)


def test_missing_required_field():
    config_data = VALID_CONFIG.copy()
    del config_data["batch_size"]

    with pytest.raises(ValidationError):
        ChurnConfig(**config_data)


def test_invalid_mode():
    config_data = VALID_CONFIG.copy()
    config_data["mode"] = "invalid_mode"

    with pytest.raises(ValidationError):
        ChurnConfig(**config_data)


def test_wrong_batch_size_type():
    config_data = VALID_CONFIG.copy()
    config_data["batch_size"] = "32"

    with pytest.raises(ValidationError):
        ChurnConfig(**config_data)