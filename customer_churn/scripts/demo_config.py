from pydantic import ValidationError

from configs.config import ChurnConfig


def show_invalid_config(title, config_data):
    print(f"\n--- {title} ---")

    try:
        ChurnConfig(**config_data)
    except ValidationError as error:
        print(error)


valid_config = {
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


print("Valid configuration:")
print(ChurnConfig(**valid_config))


show_invalid_config(
    "Invalid Config 1: Wrong batch size",
    {
        **valid_config,
        "batch_size": -10,
    },
)


show_invalid_config(
    "Invalid Config 2: Invalid threshold",
    {
        **valid_config,
        "threshold": 1.5,
    },
)


show_invalid_config(
    "Invalid Config 3: Invalid data path",
    {
        **valid_config,
        "data_path": "data/raw/does_not_exist.csv",
    },
)

missing_batch_size_config = valid_config.copy()
del missing_batch_size_config["batch_size"]

show_invalid_config(
    "Invalid Config 4: Missing batch size",
    missing_batch_size_config,
)

show_invalid_config(
    "Invalid config 5: Invalid mode",
    {
        **valid_config,
        "mode":"testing",
    },
)

show_invalid_config(
    "Invalid config 6: Wrong batch size type",
    {
        **valid_config,
        "batch_size":"large",
    },
)