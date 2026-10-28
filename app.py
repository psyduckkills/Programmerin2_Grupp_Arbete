
import plotly.express as px
from flask import Flask, jsonify, render_template

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

