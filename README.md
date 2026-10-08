# dfinsight

A lightweight Python library for initial dataset inspection and basic data-quality assessment using pandas.

## Features

- Dataset dimensions
- Data types
- Missing-value counts
- Missing-value percentages
- Missing-value severity
- Duplicate-row detection
- Numeric summary
- Basic issue detection

## Installation

```bash
pip install dfinsight-kit
````

## Example

```python
import pandas as pd
from dfinsight import quality_report

df = pd.read_csv("data.csv")

quality_report(df)
```

## What it checks

`dfinsight` provides a quick first look at a pandas DataFrame and highlights basic data-quality issues such as:

* Missing values
* High levels of missingness
* Duplicate rows
* Column data types
* Basic numerical statistics

The missing-value severity levels are heuristic indicators intended to support initial dataset investigation.

## Links

- [PyPI Package](https://pypi.org/project/dfinsight-kit/)

## Version

0.1.0
