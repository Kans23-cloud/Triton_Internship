from enum import Enum
from pathlib import Path

from pydantic import BaseModel, StrictFloat, StrictInt, Field, field_validator


class Mode(str, Enum):
    TRAIN = "train"
    PREDICT = "predict"
    EVALUATE = "evaluate"


class Device(str, Enum):
    CPU = "cpu"
    CUDA = "cuda"


class ChurnConfig(BaseModel):
    data_path: str

    batch_size: StrictInt = Field(
        gt=0
    )

    feature_columns: list[str] = Field(
        min_length=1
    )

    mode: Mode

    device: Device

    threshold: StrictFloat = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
    )

    @field_validator("data_path")
    @classmethod
    def validate_data_path(cls, value):
        path = Path(value)

        if not path.is_file():
            raise ValueError(
                f"data_path does not exist or is not a file: {value}"
            )

        return value