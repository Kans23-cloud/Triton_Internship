from configs.config import ChurnConfig

config = ChurnConfig(
    data_path="data/raw/customers.csv",
    batch_size=32,
    feature_columns=[
        "tenure",
        "monthly_charges",
        "customer_value",
    ],
    mode="train",
    device="cpu",
    threshold=0.5,
)

print(config)