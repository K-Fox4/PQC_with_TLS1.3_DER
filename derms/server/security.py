from hmac import compare_digest
from models import DERGatewayModel


def authenticate(username, password):
    gateway = DERGatewayModel.find_by_username(username=username)
    if gateway and compare_digest(gateway.password, password):
        return gateway


def identity(payload):
    gateway_id = payload["identity"]
    return DERGatewayModel.find_by_gateway_id(gateway_id=gateway_id)
