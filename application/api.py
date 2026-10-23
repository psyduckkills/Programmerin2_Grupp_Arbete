import requests

URL="https://archive-api.open-meteo.com/v1/archive"

#class ApiFel(Exception):  #När data inte kan hämtas


def hamta_vaderdata(lat=59.33, lon=18.07, start="2000-01-01", slut="2026,10,23"):
    params={
        "latitud":lat,
        "longitud":lon,
        "start_datum":"start",
        "slut_datum":"slut",
        "daglig": "temperature_2m_mean,precipitation_sum",
        "tidszon": "Europa/Stockholm",
    }

    try:
        svar= requests.get(URL,params=params, timeout=10)
        svar.raise_for_status()
    except requests.exceptions.RequestException:
        return None
    print("URL: ",svar.url)
    print("Status: ",svar.status_code)
    print("Svar: ", svar.text[:200])
    return svar.json()