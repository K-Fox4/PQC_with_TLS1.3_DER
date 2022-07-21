from flask import Flask, render_template
from flask_restful import Api

from utils import (
    get_all_unique_der_networks,
    generate_pow_vs_time_plots_all_der_networks,
)
from resources import DERInfo
from db import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///der_data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "KaLyAnNaKkA"

db.init_app(app=app)

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/")
def home():
    return render_template("home.html",
                           title="Home",
                           ders=get_all_unique_der_networks())


@app.route("/monitor")
def monitor():
    generate_pow_vs_time_plots_all_der_networks()
    return render_template("monitor.html",
                           title="Monitor",
                           ders=get_all_unique_der_networks())


@app.route("/about")
def about():
    return render_template("about.html",
                           title="About")


# /derinfo URI
api.add_resource(DERInfo, "/derinfo")


if __name__ == '__main__':
    app.run(port=5684, debug=True)
