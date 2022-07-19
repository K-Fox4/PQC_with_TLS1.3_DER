from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources import DERInfo, GatewayRegister
from security import authenticate, identity
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


# /auth URI
jwt = JWT(
    app=app,
    authentication_handler=authenticate,
    identity_handler=identity
)

# /derinfo URI
api.add_resource(DERInfo, "/derinfo")

# /gway_register URI
api.add_resource(GatewayRegister, "/gway_register")


if __name__ == '__main__':
    app.run(port=5684)
