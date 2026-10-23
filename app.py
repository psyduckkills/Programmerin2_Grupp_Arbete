
from flask import Flask, jsonify, render_template

from application.func import hamta_vaderdata, medel_temp_per_manad, nederbord_per_manad

from datetime import date
import calendar
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
import requests
import pandas as pd




app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vader")
def vader_overvy():
    data = medel_temp_per_manad()
    return render_template("vader.html", data=data)

@app.route("/vader/nederbord")
def nederbord():
    data = nederbord_per_manad()
    return render_template("nederbord.html", data=data)

@app.route("/api/vader")
def api_vader():
    data = hamta_vaderdata()
    return jsonify(data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(host='127.0.0.1', port = 5000, debug=True)

    
'''

@TBD.route("/api", methods=["POST"])  #API och våra tre frågor
def api():
    ar= request.form.get("ar", type=int)
    manad= request.form.get("manad", type=int)
    nederbord= request.form.get("nederbord")
    temp=request.form.get("temp")

    if None in (ar, manad):
        return render_templates("fel.html", medde= "Fyll i år och månad med siffror")

    if not 2000 <= ar <= 2026:
        return render_templates("fel.html", medde= "Året måste vara mellan år 2000 och år 2026")

    try:                #felsökning när API anropas
        date(ar, manad)
        return render_template("fel.html", medde= "Datumet finns inte." ), 400
    except ValueError:
        return render_template("fel.html", medde="Datumet finns inte."),400
    URL_ned= (f"https://open-meteo.com/en/docs/historical-weather-api" f"{ar}/{manad}_{nederbord}.json")
    URL_temp= (f"https://open-meteo.com/en/docs/historical-weather-api" f"{ar}/{manad}_{temp}.json")

    try:
        svar= requests.get(URL_ned, URL_temp, timeout=5)
    except requests.exeptions.RequestException:
        return render_template("fel.html", medde= "kunde inte nå efterfrågan, försök igen om en stund."),502

    if svar.status_code==404:
        return render_template("fel.hmlt", medde="Det finns ingen statestik för denna datum.")

    svar.raise_for_status()

    nederbord=pd.DataFrame(svar.json())
    svar.rais_for_status()

    temp=pd.DataFrame(svar.json())
    svar.rais_for_status()

    return render_template( "resultat.html", nederbord=html, temp=html, ar=ar, manad=manad)

'''

######Börjar så, vet inte hur saker ser ut än###########
