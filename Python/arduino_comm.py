# https://pyserial.readthedocs.io/en/latest/shortintro.html
# https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0#:~:text=check%20your%20installation.-,Step%203%3A%20Python%20Code,-First%20up%2C%20we

import argparse
import serial
import time
# import pandas as pd

# TODO
# install conda on pi
# create Environment with requirement.txt
# install pandas to it

COMMAND_MAP = {
    1: "Collect all data [Soil moisture %]",
    2: "Collect Soil Moisture Percent"
}

def main(commands):
    
    for command in commands:
        have_info=False
        print(f"Waiting for data from command: {COMMAND_MAP[command]}...")
        while not have_info:
            print("...")
            arduino.write(bytes(str(command), 'utf-8'))
            time.sleep(0.05)
            while True:
                data = arduino.readline()
                if data==b'':
                    break
                plant_data = data
                have_info=True
            if data is None:
                have_info = False
        plant_data = plant_data.decode('UTF-8').split(',')[:-1]
        # print(plant_data.split(',')[:-1])
        print(plant_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Request data from the plant monitor.')
    parser.add_argument('commands', type=int, nargs='+',
                    help='The list of commands to send to the arduino separated by spaces ')

    args = parser.parse_args()
    print(f"Processing the following commands: {args.commands}")
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    main(args.commands)
