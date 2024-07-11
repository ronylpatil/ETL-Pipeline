import typing
import pandas as pd


def preprocessing(df: pd.DataFrame) -> pd.DataFrame:
    # NewFeature1: trip_duration
    def calculate_trip_duration(
        pick_datetime: pd.Timestamp, drop_datetime: pd.Timestamp
    ) -> float:
        # return trip duration in minutes
        return (drop_datetime - pick_datetime).total_seconds() / 60

    # NewFeature2: speed
    def calculate_speed(dist: float, time: float) -> float:
        return dist / (time / 60)

    # NewFeature3: cost_per_mile
    def calculate_cost_per_mile(amount: float, distance: float) -> float:
        return amount / distance

    # NewFeature4: cost_per_passenger
    def calculate_cost_per_passenger(amount: float, pass_count: float) -> float:
        return amount / pass_count

    # NewFeature5: tip_percent
    def calculate_tip_percent(tip_amount: float, total_amount: float) -> float:
        return (tip_amount / total_amount) * 100

    # drop columns having maximum NULL values
    df.drop(columns=["congestion_surcharge", "airport_fee"], axis=1, inplace=True)

    # drop rows where passenger_count, RatecodeID, store_and_fwd_flag is NULL
    df.dropna(inplace=True)

    # drop the rows where
    #       - trip_distance = 0
    #       - trip_duration = 0
    #       - total_amount = 0
    #       - passenger_count = 0
    df.drop(df.loc[df["trip_distance"] == 0].index, inplace=True)
    df.drop(df.loc[df["trip_duration"] == 0].index, inplace=True)
    df.drop(df.loc[df["total_amount"] == 0].index, inplace=True)
    df.drop(df.loc[df["passanger_count"] == 0].index, inplace=True)

    df["trip_duration"] = df.apply(
        lambda x: calculate_trip_duration(
            x["tpep_pickup_datetime"], x["tpep_dropoff_datetime"]
        ),
        axis=1,
    )

    df["speed"] = df.apply(
        lambda x: calculate_speed(x["trip_distance"], x["trip_duration"]), axis=1
    )

    df["cost_per_mile"] = df.apply(
        lambda x: feature_cost_per_mile(x["total_amount"], x["trip_distance"]), axis=1
    )

    df["cost_per_passanger"] = df.apply(
        lambda x: calculate_cost_per_passenger(x["total_amount"], x["passenger_count"]),
        axis=1,
    )

    df["tip_percent"] = df.apply(
        lambda x: calculate_tip_percent(x["tip_amount"], x["total_amount"]), axis=1
    )

    return df
