import json
import random
import time
import settings

from typing import List
from datetime import datetime, timezone
from message import Message


class Meter:
    """
    Meter is a simulated energy meter
    """

    @staticmethod
    def consumption() -> int:
        '''
        Mock regular home power consumption in watts
        :return: int
        '''
        return random.randint(0, 9000)

    def __init__(self, current_value: int = 0):
        """
        :param current_value: sets the starting meter value
        in watt hours (default 0)
        """
        self.__meter_value = current_value
        self.sample_rate = settings.sample_rate

    def get_meter_value(self) -> List[str]:
        """
        :return: List of current meter value and time sampled.
        """

        return [self.__meter_value, datetime.now(timezone.utc).isoformat()]

    def update_meter_value(self) -> None:
        """
        Updates meter value with the consumption value
        :return: None
        """
        self.__meter_value = self.__meter_value + Meter.consumption()

        return None

    def meter_run(self, start: bool = False) -> None:
        """
        Takes samples of the meter and send them to the message
        broker as JSON format
        Settings.py - Meter config - sets the sample rate
        :param start: starts and stops meter - default True
        :return: None
        """

        while start:
            # creates a message handler
            meter_messenger = Message()

            # Updates the energy consumption
            self.update_meter_value()

            # send an update to the message broker
            meter_output = self.get_meter_value()
            meter_dict = {"value": str(meter_output[0]),
                          "sample_time": str(meter_output[1])}
            meter_message = json.dumps(meter_dict)
            meter_messenger.publish(meter_message)

            time.sleep(self.sample_rate)

        return None
