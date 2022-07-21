import os
import matplotlib.pyplot as plt

from models import DERInfoModel, DERAllInfoModel


def get_all_unique_der_networks():
    return list(map(lambda x: x.json(), DERInfoModel.query.all()))


def generate_pow_vs_time_plots_all_der_networks():
    unique_der_networks = get_all_unique_der_networks()

    for der_network in unique_der_networks:
        all_data_records = list(map(lambda x: x.json(), DERAllInfoModel.find_all_by_sfdi(sfdi=der_network["sfdi"])))
        x_axis_data = [int(val["passed_time"]) for val in all_data_records]
        y_axix_data = [float(val["ess_qe"]) for val in all_data_records]

        fig, ax = plt.subplots()
        ax.set(title="Reactive Power output of ESS",
               xlabel="Time (sec)",
               ylabel="Reactive Power (MVar)")
        plt.plot(x_axis_data, y_axix_data, "b-")
        plt.ylim(-2.0, 2.0)
        plt.grid(b=True, which="major", color="0.6", linestyle="--")
        plt.savefig(os.path.join("static", "images", f"pow_vs_time_plot_{der_network['sfdi']}.svg"))


if __name__ == '__main__':
    generate_pow_vs_time_plots_all_der_networks()
