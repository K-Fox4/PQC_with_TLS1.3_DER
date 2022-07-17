from flask import Flask, jsonify, request

app = Flask(__name__)


# Home endpoint, can be used for testing
@app.route("/")
def home():
    return "PQC-enabled TLS 1.3 based HTTPS environment for DERMS & DER Network"


# POST endpoint, to save the DER Network information

# DER Network information JSON structure
# {
#   "mf_model": "Model-1",
#   "sfdi": "097935300833",
#   "battery_status": "3",
#   "ess_qe": "1.0",
#   "passed_time": "25",
#   "current_power_source": "1",
#   "command": "0"
# }

@app.route("/der", methods=["POST"])
def save_der_network_info():
    request_data = request.get_json()


if __name__ == "__main__":
    app.run(port=5684)
