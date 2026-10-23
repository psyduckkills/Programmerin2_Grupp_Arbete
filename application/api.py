import requests

URL="https://archive-api.open-meteo.com/v1/archive"

#class ApiFel(Exception):  #När data inte kan hämtas


def hamta_vaderdata(lat=59.33, lon=18.07, start="2025-01-01", slut="2025-01-05"):
    params={
        "latitude":lat,
        "longitude":lon,
        "start_date":start,
        "end_date":slut,
        "daily": "temperature_2m_mean,precipitation_sum",
        "timezone": "Europe/Stockholm",
    }

    try:
        svar= requests.get(URL,params=params, timeout=10)
        svar.raise_for_status()
        return svar.json()
    except requests.exceptions.RequestException as fel:
        print("FEL:", fel)
        return None
