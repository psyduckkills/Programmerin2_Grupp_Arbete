
import plotly.express as px
from flask import Flask, jsonify, render_template, request
from datetime import date
import plotly.graph_objects as go

from application.api import hamta_vaderdata
from application.funk import (
    medel_temp_per_manad,
    nederbord_per_manad,
    till_dataframe,
    vader,
)

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template("index.html")
'''
sample_data = pd.DataFrame({
    "category": ["A", "B", "C", "D"],
    "value": [42, 17, 35, 29],
})

'''


@app.route("/vader", methods=["GET"])
def vader_overvy():
    vaderdata=hamta_vaderdata()
    if vaderdata is None:
        return render_template("fel.html", meddelande="Kunde inte hämta väderdata.")
    else:
        df = till_dataframe(vaderdata)
        df = df.rename(columns={
            "temperature_2m_min": "temperatur",
            "dag": "Dag"
            })
        fig = px.line(df, x="Dag", y="temperatur", title="Väder")
        chart_html = fig.to_html(full_html=False, include_plotlyjs="cdn")
        return render_template("vader.html", data= vader(vaderdata), chart=chart_html)

@app.route("/vader/nederbord", methods=["GET"])
def nederbord():
    vaderdata=hamta_vaderdata()
    if vaderdata is None:
        return render_template("fel.html", meddelande="Kunde inte hämta väderdata")
    else:
        df = till_dataframe(vaderdata)
        df = df.rename(columns={
                               "manad": "Månad",
                               "precipitation_sum": "Total nederbörd per mm"
                               })
        fig = px.bar(df, x="Månad", y="Total nederbörd per mm", title="Nederbörd per Månad")
        chart_html = fig.to_html(full_html=False, include_plotlyjs="cdn")
        return render_template("nederbord.html", data=nederbord_per_manad(vaderdata), chart=chart_html)

@app.route("/medeltemp", methods=["GET"])
def medeltemp():
    vaderdata=hamta_vaderdata()

    if vaderdata is None:
        medel_temp_per_manad(vaderdata)
        return render_template("fel.html", meddelande="Kunde inte hämta väderdata.")

    else:
        df = till_dataframe(vaderdata)
        df = df.rename(columns={
            "manad": "Månad",
            "temperature_2m_mean": "Medeltemp"
            })
        fig = px.line(df, x="Månad", y="Medeltemp", title="Medeltemperatur per Månad")
        chart_html = fig.to_html(full_html=False, include_plotlyjs="cdn")
        return render_template("medeltemp.html", data=medel_temp_per_manad(vaderdata), chart = chart_html)

@app.route("/datum", methods=["GET", "POST"])
def filtrerad_datum():
    error = None
    selected_date = None
    mean_temp = None
    min_temp = None
    max_temp = None
    precipitation = None
    plot_html = None

    # Load weather data
    vaderdata = hamta_vaderdata()

    if vaderdata is None:
        return render_template(
            "fel.html",
            meddelande="Kunde inte hämta väderdata."
        )
    # tar emot variablerna från Json filen med vår väder data
    daily = vaderdata["daily"]
    dates = daily["time"]

    if request.method == "POST":
        try:
            # Variablerna som formuläret skickar
            day = int(request.form["day"])
            month = int(request.form["month"])
            year = int(request.form["year"])

            # formulerar om datumet till YYYY-MM-DD format
            selected_date = date(year, month, day).isoformat()

            dates = daily["time"]

            # Letar efter den valda datumet och jämför med JSON datat
            if selected_date not in dates:
                raise ValueError(
                    "Det finns ingen väderdata för detta datum."
                )
            # en counter för att hitta den rätta indexet i listorna
            i = dates.index(selected_date)

            # Hitta den rätta informationen med index
            mean_temp = daily["temperature_2m_mean"][i]
            min_temp = daily["temperature_2m_min"][i]
            max_temp = daily["temperature_2m_max"][i]
            precipitation = daily["precipitation_sum"][i]

            # Skapa Plotly chart
            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=["Minimum", "Medel", "Maximum"],
                y=[min_temp, mean_temp, max_temp],
                marker_color=["#4C78A8", "#F2CF5B", "#E45756"]
            ))

            fig.update_layout(
                title=f"Väder den {selected_date}",
                xaxis_title="Temperaturtyp",
                yaxis_title="Temperatur (°C)",
                template="plotly_white"
            )

            plot_html = fig.to_html(
                full_html=False,
                include_plotlyjs="cdn"
            )

        except (ValueError, KeyError) as e:
            error = str(e) or "Kontrollera det valda datumet finns."
            selected_date = None

    return render_template(
        "datum.html",
        error=error,
        selected_date=selected_date,
        mean_temp=mean_temp,
        min_temp=min_temp,
        max_temp=max_temp,
        precipitation=precipitation,
        plot_html=plot_html
    )


@app.route("/api/vader", methods=["GET"])
def api_vader():
    data = hamta_vaderdata()
    if data is None:
        return render_template("500.html")
    else:
        return jsonify(data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(host='127.0.0.1', port = 5000, debug=True)

