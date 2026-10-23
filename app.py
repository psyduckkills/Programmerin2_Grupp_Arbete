
from flask import Flask, jsonify, render_template
from application.func import hamta_vaderdata, medel_temp_per_manad, nederbord_per_manad
import calendar from datetime import date
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
