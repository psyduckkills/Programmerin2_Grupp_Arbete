import requests

URL="https://archive-api.open-meteo.com/v1/archive"


def hamta_vaderdata(lat=59.33, lon=18.07, start="2024-01-01", slut="2026-10-23"):  #Funktion som hämtar data, lat och lon är koordinater till stockholm, start och slut är datum
    params={
        "latitude":lat,
        "longitude":lon,
        "start_date":start,
        "end_date":slut,
        "daily": "temperature_2m_mean,temperature_2m_min,temperature_2m_max,precipitation_sum", #mäter temperatur, medelvärde  och  nederbörd och summan av nederbördet
        "timezone": "Europe/Stockholm",
    }

    try:
        svar= requests.get(URL,params=params, timeout=10) #get skickar anropet, parms bygger ihop URL,anrop ger upp efter 10sek
        svar.raise_for_status() #400 och 500 skapas här 
        return svar.json()
    except requests.exceptions.RequestException as fel:
        print("FEL:", fel)
        return None
