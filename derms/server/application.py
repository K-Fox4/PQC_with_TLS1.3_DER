from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
app.secret_key = "KaLyAnNaKkA"
api = Api(app)


class DERInfo(Resource):

    def get(self):
        return {
            "message": "PQC-enabled TLS 1.3 based HTTPS environment for DERMS & DER Network"
        }


api.add_resource(DERInfo, "/derinfo")

if __name__ == '__main__':
    app.run(port=5684)
