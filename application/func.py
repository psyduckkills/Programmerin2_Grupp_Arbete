from collections import defaultdict
from datetime import datetime

import requests

LAT = 59.33
LON = 18.07

def hamta_vaderdata():
    url = "https://api.openweathermap.org/data/2.5"
    
    params = {
        "lat": LAT,
        "lon": LON,
        "exclude": "current,minutely,hourly,alerts",
        "units": "metric",
        
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("daily", [])

def medel_temp_per_manad():
    dagsdata = hamta_vaderdata()
    monthly = defaultdict(lambda: {"temp_sum":0, "days":0})

    for dag in dagsdata:
        dt = datetime.fromtimestamp(dag["dt"])
        month_key = dt.strftime("%Y-%m")
        temp = dag["temp"]["day"]  # dagstemperatur
        monthly[month_key]["temp_sum"] += temp
        monthly[month_key]["days"] += 1

    result = []
    for month, values in monthly.items():
        avg_temp = values["temp_sum"] / values["days"]
        result.append({"month": month, "avg_temp": round(avg_temp, 1)})
    return result

def nederbord_per_manad():
    dagsdata = hamta_vaderdata()
    monthly = defaultdict(lambda: {"precip_sum":0, "days":0})

    for dag in dagsdata:
        dt = datetime.fromtimestamp(dag["dt"])
        month_key = dt.strftime("%Y-%m")
        precip = dag.get("rain", 0) + dag.get("snow", 0)
        monthly[month_key]["precip_sum"] += precip
        monthly[month_key]["days"] += 1

    result = []
    for month, values in monthly.items():
        total_precip = values["precip_sum"]
        result.append({"month": month, "total_precip": round(total_precip, 1)})
    return result

