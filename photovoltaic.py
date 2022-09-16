import json
import time
import message

from typing import Tuple
from scipy.stats import norm
from datetime import datetime

import settings


class Photovoltaic:

    def __init__(self):

        self.results_file = settings.results_file
        self.sample_rate = settings.sample_rate


    @ staticmethod
    def power_model(at_hour: int, and_minute: int = 0) -> int:

        """
        Using the normal distribution; at a specific time the
        power of the PV is known
        :param int at_hour: hour of the day 24 hour format
        :param int and_minute: minute pass the hour
        :return: power at the hour and minute as float - in kW
        """
        __pv_power = 0.0
        __model_mean = 14
        __sigma = 2.5

        # adjust minutes
        adj_minute = round((1 / 60 * and_minute), 2)

        # using x find y
        pv_power = norm.pdf((at_hour + adj_minute), __model_mean, __sigma)

        # multiply out for the real number
        return round((pv_power * 20), 1)

    def persist_values(self, line: Tuple) -> None:
        """
        Write results out to file as:
            meter_sample_time, meter_sample_value in kW, pv_power kW,
            sum_of_power (meter+pv power)
        :return: None
        """
        with open(self.results_file, "a") as results_file:
            for item in line:
                results_file.write(f"{item} ")
            results_file.write("\n")
            results_file.close()

        return None

    def process_power(self) -> None:
        """
        Use the power model add this value to the meter value
        (adjusted on time) and output the result
        :return:
        """
        message_box = message.Message()
        # meter_message is None if message_box is empty
        meter_message = message_box.consume()

        if meter_message is not None:
            # message to JSON
            msg = json.loads(meter_message.decode("utf-8"))

            meter_sample_value = (msg['value'])
            meter_sample_time = \
                datetime.fromisoformat(msg['sample_time']).time()

            # using the model calculate the pv power for the sample time.
            pv_power = Photovoltaic.power_model(meter_sample_time.hour,
                                                meter_sample_time.minute)
            sum_of_power = \
                round((int(meter_sample_value) / 1000) + pv_power, 3)

            # write out results normalised in kW
            to_log = [msg['sample_time'], (int(meter_sample_value) / 1000),
                      pv_power, sum_of_power]
            self.persist_values(to_log)

        return None

    def photovoltaic_run(self, start: bool = False) -> None:
        """
        Starts a pv instance which performs the function of a simulated pv
        :param start boolean
        :return: None
        """
        while start:
            pv = Photovoltaic()
            # ingest messages
            pv.process_power()

            time.sleep(self.sample_rate - 0.5)

        return None






