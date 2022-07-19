from flask_restful import Resource, reqparse

from models import DERGatewayModel


class GatewayRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="This field cannot be blank"
    )

    def post(self):
        data = GatewayRegister.parser.parse_args()

        if DERGatewayModel.find_by_username(username=data["username"]):
            return {
                "message": "A Gateway with that username already exists"
                   }, 400

        user = DERGatewayModel(
            username=data["username"],
            password=data["password"]
        )
        user.save_to_db()

        return {
                   "message": "User created successfully"
               }, 201
