import glob

import pandas as pd
from conftest import LAB

from src.checks import COLUMNS, RESTAURANTS, problems


def test_base_data_schema_and_ranges(base):
    df = base
    assert list(df.columns) == COLUMNS
    assert not df.isna().any().any()
    assert df["distance_km"].between(0.1, 50).all()          # every value is inside a range
    assert df["restaurant"].isin(RESTAURANTS).all()          # every value is one of a list
    assert 0.1 < df["late"].mean() < 0.40           # an average is inside a range


def test_incoming_batches_pass_the_data_checks():
    """Any new file placed in data/incoming/ must pass the same checks before we train on it."""
    for path in sorted(glob.glob(str(LAB / "data" / "incoming" / "*.csv"))):
        found = problems(pd.read_csv(path))
        assert found == [], f"{path}: {found}"
