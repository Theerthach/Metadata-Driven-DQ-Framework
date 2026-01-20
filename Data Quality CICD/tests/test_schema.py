import pandas as pd
import yaml
import pytest

@pytest.mark.parametrize("file", [
    "data/good_booking.csv",
    "data/bad_booking.csv"
])
def test_schema_validation(file):
    try:
        df = pd.read_csv(file)
    except Exception as e:
        pytest.fail(f"Data loading failed: {e}")

    with open("rules/schema_rules.yaml") as f:
        schema = yaml.safe_load(f)["columns"]

    for column, rules in schema.items():
        assert column in df.columns, f"Missing column: {column}"

        if not rules["nullable"]:
            assert df[column].isnull().sum() == 0, f"Nulls found in {column}"