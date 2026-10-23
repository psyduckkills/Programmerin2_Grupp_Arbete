import pandas as pd


def till_dataframe(data):
    df = pd.DataFrame(data["daily"])
    df["datum"] = pd.to_datetime(df["time"])
    df["manad"] = df["datum"].dt.strftime("%Y-%m")  # ny kolumn, t.ex. "2025-01"
    return df


def medel_temp_per_manad(data):
    df = till_dataframe(data)
    medel = df.groupby("manad")["temperature_2m_mean"].mean().round(1)
    return [{"month": manad, "avg_temp": float(temp)} for manad, temp in medel.items()]


def nederbord_per_manad(data):
    df = till_dataframe(data)
    summa = df.groupby("manad")["precipitation_sum"].sum().round(1)
    return [{"month": manad, "total_precip": float(ned)} for manad, ned in summa.items()]