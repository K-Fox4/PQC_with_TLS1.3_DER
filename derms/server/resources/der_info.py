from flask_restful import Resource, reqparse

from models import DERInfoModel


class DERInfo(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "mf_model",
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument(
        "sfdi",
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument(
        "battery_status",
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument(
        "ess_qe",
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument(
        "passed_time",
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument(
        "current_power_source",
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument(
        "command",
        type=str,
        required=True,
        help="This field cannot be blank"
    )

    def get(self):
        return {
            "der_info": list(map(lambda x: x.json(), DERInfoModel.query.all()))
        }

    def post(self):
        data = DERInfo.parser.parse_args()

        der_info = DERInfoModel.find_by_sfdi(data["sfdi"])
        if der_info:
            der_info.battery_status = data["battery_status"]
            der_info.ess_qe = data["ess_qe"]
            der_info.passed_time = data["passed_time"]
            der_info.current_power_source = data["current_power_source"]
            der_info.command = data["command"]
        else:
            der_info = DERInfoModel(**data)

        der_info.save_to_db()
        return der_info.json(), 201
