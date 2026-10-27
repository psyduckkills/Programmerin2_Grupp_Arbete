
from flask import Flask, jsonify, render_template
from application.api import hamta_vaderdata
from application.funk import nederbord_per_manad, medel_temp_per_manad, vader



app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vader", methods=["GET"])
def vader_overvy():
    vaderdata=hamta_vaderdata()
    if vaderdata is None:
        return render_template("fel.html", meddelande="Kunde inte hämta väderdata.")
    return render_template("vader.html", data= vader(vaderdata))

@app.route("/vader/nederbord", methods=["GET"])
def nederbord():
    vaderdata=hamta_vaderdata()
    if vaderdata is None:
        return render_template("fel.html", meddelande="Kunde inte hämta väderdata")
    return render_template("nederbord.html", data=nederbord_per_manad(vaderdata))

@app.route("/medeltemp", methods=["GET"])
def medeltemp():
    vaderdata=hamta_vaderdata()
    if vaderdata is None:
        return render_template("fel.html", meddelande="Kunde inte hämta väderdata.")
    return render_template("medeltemp.html", data=medel_temp_per_manad(vaderdata))


@app.route("/api/vader", methods=["GET"])
def api_vader():
    data = hamta_vaderdata()
    if data is None:
        return jsonify({"fel": "Kunde inte hämta väderdata."})
    return jsonify(data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(host='127.0.0.1', port = 5000, debug=True)
