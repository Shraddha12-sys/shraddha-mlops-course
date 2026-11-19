import pandas as pd

from src.features import add_rush_flag


def test_add_rush_flag():
    # Three parts: make a tiny input, call the function, compare with the answer you worked out by hand.
        df = pd.DataFrame({"hour": [17, 18, 20, 21]})
        result = add_rush_flag(df)
        assert list(result["rush"]) == [0, 1, 1, 0]     # 1 = rush hour, 0 = not
    


def test_add_rush_flag_does_not_change_the_input():
    df = pd.DataFrame({"hour": [17, 19]})
    add_rush_flag(df)
    assert list(df.columns) == ["hour"]          # the original table is untouched
