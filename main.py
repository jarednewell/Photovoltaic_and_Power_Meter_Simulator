import threading
import logging

from meter import Meter
from photovoltaic import Photovoltaic

def main():

    logging.getLogger().setLevel(logging.INFO)

    logging.info("PV simulator started")

    # Start photovoltaic in own thread
    photovoltaic_simulator = Photovoltaic()
    photovoltaic_thread = \
        threading.Thread(target=photovoltaic_simulator.photovoltaic_run,
                         args=(True,),
                         name=photovoltaic_simulator)
    photovoltaic_thread.start()


    # Start meter in own thread
    power_meter = Meter()
    meter_thread = threading.Thread(target=power_meter.meter_run,
                                    args=(True,),
                                    name=power_meter)
    meter_thread.start()

if __name__ == '__main__':
    main()









