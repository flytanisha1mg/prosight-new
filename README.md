# prosight-new

This repository contains a small example dataset and a helper script
for building time series with the [`darts`](https://github.com/unit8co/darts)
library.

## Usage

1. Install the dependencies (see `requirements.txt` or simply install
   `darts` with pip).
2. Run `process_data.py` to load the CSV file and create grouped time
   series objects.

```bash
python process_data.py
```

The script uses `TimeSeries.from_group_dataframe` and **expects the input
DataFrame to contain only the grouping columns, the metric columns and
the date column**. It also resets the index before creating the
`TimeSeries` objects:

```python
# keep only the required columns
df = df[GROUP_COLS + METRICS + ['date']].copy()

# reset index and ensure date type
df['date'] = pd.to_datetime(df['date'])
df = df.reset_index(drop=True)
```

Make sure to perform these steps on any DataFrame you pass to
`TimeSeries.from_group_dataframe` to avoid hidden `MultiIndex`
issues.
