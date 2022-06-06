import argparse
import serial
import time
import pandas as pd
import yaml


def main(args, config):
    if args.verbose > 0:  # This print statement will only appear if the -v flag is set
        print(f"Processing the following commands: {args.commands}")

    for command in args.commands:
        if command not in config['command_map'].keys():  # Check that we received a valid command
            print(f"Unrecognized command: {command}")
            raise ValueError
            continue

        have_info=False

        if args.verbose > 0:
            print(f"Waiting for data from command: {config['command_map'][command]}",end='',flush=True)

        while not have_info:
            if args.verbose > 0:  
                print(".", sep='', end='', flush=True)

            arduino.write(bytes(str(command), 'utf-8'))  # Send our command to the Arduino
            time.sleep(0.05)  # Wait for data to arrive
            data = arduino.readline()  # Read what was sent from the Arduino

            if data!=b'':  # Break condition: when we receive non-empty data we will record it and break the while loop
                data = data.decode('UTF-8').split(',')[:-1]
                have_info=True

        if args.verbose > 0:
            print(" done!")
            if args.verbose > 1:
                print(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Request data from the plant monitor.')
    parser.add_argument('commands', type=int, nargs='+',
                    help='The list of commands to send to the arduino separated by spaces ')
    parser.add_argument('--verbose', '-v', action='count', default=0)
    args = parser.parse_args()

    with open('config.yaml') as f:
        config = yaml.safe_load(f)

    arduino = serial.Serial(config['port'], 9600, timeout=1)

    main(args, config)
