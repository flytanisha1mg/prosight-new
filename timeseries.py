import pandas as pd
from darts import TimeSeries
from darts.models import NBEATSModel
from darts.metrics import mape
import matplotlib.pyplot as plt


def main():
    # Load dataset
    df = pd.read_csv("prolabs_gmv_2020.csv", parse_dates=["date"])

    # Create a TimeSeries using the completed GMV column
    series = TimeSeries.from_dataframe(df, time_col="date", value_cols="completed_gmv")

    # Split into training and validation sets
    train, val = series[:-30], series[-30:]

    # Initialize and train the model
    model = NBEATSModel(input_chunk_length=20, output_chunk_length=10, n_epochs=50, random_state=0)
    model.fit(train)

    # Predict the next 30 time steps
    forecast = model.predict(n=30)

    # Evaluate accuracy
    print("MAPE:", mape(val, forecast))

    # Plot actual vs forecast
    series.plot(label="actual")
    forecast.plot(label="forecast")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
