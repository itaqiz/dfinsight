
import pandas as pd


def missing_percentage(df):
    mp = df.isna().sum() / len(df) * 100
    return mp


def missing_severity(percent):

    if percent == 0:
        return "None"

    elif percent <= 5:
        return "LOW"

    elif percent <= 20:
        return "MEDIUM"

    else:
        return "HIGH"


def quality_report(df):
    print("=" * 50)
    print("DFINSIGHT REPORT")
    print("=" * 50)

    print("\nDATASET")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    print("\nDATA TYPES")
    print(df.dtypes)

    print("\nMISSING VALUES")
    print(df.isna().sum())

    print("\nMISSING PERCENTAGE")
    print(missing_percentage(df))

    print("\nDUPLICATE ROWS")
    print(df.duplicated().sum())

    print("\nNUMERIC SUMMARY")
    print(df.describe())

    print("\nISSUES DETECTED")

    for column in df.columns:
        missing = df[column].isna().sum()

        if missing > 0:
            percentage = missing / len(df) * 100
            severity = missing_severity(percentage)

            print(
                f"- Missing values in '{column}': "
                f"{missing} ({percentage:.1f}%) "
                f"[{severity}]"
            )

    duplicates = df.duplicated().sum()

    if duplicates > 0:
        print(f"- Duplicate rows detected: {duplicates}")

    print("\n" + "=" * 50)
