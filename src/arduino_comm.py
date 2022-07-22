import argparse
import serial
import time


def send_cmd(args, port, command_map):
    arduino = serial.Serial(port, 9600, timeout=1)

    if args.verbose > 0:  # This print statement will only appear if the -v flag is set
        print(f"Processing the following commands: {args.commands}")

    next_cmd_is_val = False
    for command in args.commands:
        if not next_cmd_is_val and command not in command_map.keys():  # Check that we received a valid command
            print(f"Unrecognized command: {command}")
            raise ValueError
            continue

        if args.verbose > 0 and not next_cmd_is_val:
            print(f"Waiting for data from command {command}: {command_map[command]}",end='',flush=True)

        next_cmd_is_val = False
        have_info=False

        while not have_info:
            if args.verbose > 0:  
                print(".", sep='', end='', flush=True)

            arduino.write(bytes(str(command), 'utf-8'))  # Send our command to the Arduino
            if command == 3:  # Command 3 (water) needs an argument (seconds to pump)
                next_cmd_is_val = True
            time.sleep(0.05)  # Wait for data to arrive
            data = arduino.readline()  # Read what was sent from the Arduino

            if data!=b'':  # Break condition: when we receive non-empty data we will record it and break the while loop
                data = data.decode('UTF-8').split(',')[:-1]
                have_info=True

        if args.verbose > 0:
            print(" done!")
            if args.verbose > 1:
                print(data)
    return data


if __name__ == "__main__":
    pass
