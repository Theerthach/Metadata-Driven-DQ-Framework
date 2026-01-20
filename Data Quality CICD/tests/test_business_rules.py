import pandas as pd
from datetime import datetime
import pytest

@pytest.mark.parametrize("file", [
    "data/good_booking.csv",
    "data/bad_booking.csv"
])

def test_business_rules(file):
    df = pd.read_csv(file)

    # Fare must be > 0
    assert (df["fare"] > 0).all(), "Fare must be positive"

    # Allowed status values
    allowed_status = ["CONFIRMED", "CANCELLED"]
    assert df["status"].isin(allowed_status).all(), "Invalid status found"

    # Flight date must be after booking date
    df["flight_date"] = pd.to_datetime(df["flight_date"])
    df["booking_date"] = pd.to_datetime(df["booking_date"])

    assert (df["flight_date"] >= df["booking_date"]).all(), \
        "Flight date before booking date"