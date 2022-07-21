from db import db


class DERAllInfoModel(db.Model):

    __tablename__ = "der_all_info"

    der_id = db.Column(db.Integer, primary_key=True)
    der_name = db.Column(db.String(80))
    mf_model = db.Column(db.String(80))
    sfdi = db.Column(db.String(80))
    battery_status = db.Column(db.String(80))
    ess_qe = db.Column(db.String(80))
    passed_time = db.Column(db.String(80))
    current_power_source = db.Column(db.String(80))
    command = db.Column(db.String(80))

    def __init__(self,
                 der_name,
                 mf_model,
                 sfdi,
                 battery_status,
                 ess_qe,
                 passed_time,
                 current_power_source,
                 command):
        self.der_name = der_name
        self.mf_model = mf_model
        self.sfdi = sfdi
        self.battery_status = battery_status
        self.ess_qe = ess_qe
        self.passed_time = passed_time
        self.current_power_source = current_power_source
        self.command = command

    def json(self):
        return {
            "der_name": self.der_name,
            "mf_model": self.mf_model,
            "sfdi": self.sfdi,
            "battery_status": self.battery_status,
            "ess_qe": self.ess_qe,
            "passed_time": self.passed_time,
            "current_power_source": self.current_power_source,
            "command": self.command,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_all_by_sfdi(cls, sfdi):
        return cls.query.filter_by(sfdi=sfdi).all()
