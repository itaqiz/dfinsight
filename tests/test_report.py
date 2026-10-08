
import pandas as pd

from dfinsight import missing_percentage, missing_severity


def test_missing_percentage():
    df = pd.DataFrame({
        "age": [20, None, 30, 40]
    })

    result = missing_percentage(df)

    assert result["age"] == 25.0


def test_missing_severity():
    assert missing_severity(0) == "None"
    assert missing_severity(3) == "LOW"
    assert missing_severity(10) == "MEDIUM"
    assert missing_severity(40) == "HIGH"
