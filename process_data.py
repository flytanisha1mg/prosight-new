import pandas as pd
from darts import TimeSeries

# Example of reading the dataset and converting to a list of TimeSeries
CSV_FILE = 'prolabs_gmv_2020.csv'
GROUP_COLS = ['is_droplet', 'status']
METRICS = ['placed_gmv', 'delivered_gmv', 'cancelled_gmv', 'completed_gmv']

def load_series(csv_path: str = CSV_FILE):
    """Load the CSV and convert grouped data to TimeSeries objects."""
    df = pd.read_csv(csv_path)

    # Keep only the necessary columns before creating the TimeSeries
    df = df[GROUP_COLS + METRICS + ['date']].copy()

    # Ensure a clean index and proper date dtype
    df['date'] = pd.to_datetime(df['date'])
    df = df.reset_index(drop=True)

    series_list = TimeSeries.from_group_dataframe(
        df,
        group_cols=GROUP_COLS,
        time_col='date',
        value_cols=METRICS,
        fill_missing_dates=True,
        freq="D",
    )

    return series_list

if __name__ == '__main__':
    series = load_series()
    print(f"Loaded {len(series)} time series")
