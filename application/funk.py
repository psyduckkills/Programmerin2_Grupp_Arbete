import pandas as pd


def till_dataframe(data):    #funktion med pandas för tabell och kolumner
    df = pd.DataFrame(data["daily"])
    df["datum"] = pd.to_datetime(df["time"])
    df["manad"] = df["datum"].dt.strftime("%y-%m")
    df["dag"]= df["datum"].dt.strftime("%y-%m-%d")
    return df


def medel_temp_per_manad(data):  #
    df = till_dataframe(data)
    medel = df.groupby("manad")["temperature_2m_mean"].mean().round(1)  #delar upp månad och temperatur i olika kolumner 
    return [{"month": manad, "avg_temp": float(temp)} for manad, temp in medel.items()]


def nederbord_per_manad(data):
    df = till_dataframe(data)
    summa = df.groupby("manad")["precipitation_sum"].sum().round(1)
    return [{"month": manad, "total_precip": float(ned)} for manad, ned in summa.items()]

def vader(data):
    df = till_dataframe(data)
    resultat=df.groupby("manad").agg ( min_temp=("temperature_2m_min","min"), max_temp=("temperature_2m_max","max")).round(1) #agg kan räkna ut flera saker samtidig
    resultat= resultat.reset_index().rename(columns={"manad":"month"})
    return resultat.to_dict("records")

