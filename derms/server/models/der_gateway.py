from db import db


class DERGatewayModel(db.Model):

    __tablename__ = "der_gateways"

    gateway_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_gateway_id(cls, gateway_id):
        return cls.query.filter_by(gateway_id=gateway_id).first()
