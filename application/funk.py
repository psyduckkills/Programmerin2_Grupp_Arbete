import pandas as pd


def till_dataframe(data):    #funktion med pandas för tabell och kolumner
    df = pd.DataFrame(data["daily"])
    df["datum"] = pd.to_datetime(df["time"])
    df["manad"] = df["datum"].dt.strftime("Y-M")  
    return df


def medel_temp_per_manad(data):
    df = till_dataframe(data)
    medel = df.groupby("manad")["temperature_2m_mean"].mean().round(1)  #delar upp månad och temperatur i olika kolumner 
    return [{"month": manad, "avg_temp": float(temp)} for manad, temp in medel.items()]


def nederbord_per_manad(data):
    df = till_dataframe(data)
    summa = df.groupby("manad")["precipitation_sum"].sum().round(1)
    return [{"month": manad, "total_precip": float(ned)} for manad, ned in summa.items()]

def vader(data):
    df = till_dataframe(data)
    summa = df.groupby("manad")["temperature_2m"].sum().round(1)
    return [{"month": manad, "temp": float(ned)} for manad, ned in summa.items()]