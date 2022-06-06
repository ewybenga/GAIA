import argparse
import yaml

from src.arduino_comm import send_cmd

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Request data from the plant monitor.')
    parser.add_argument('commands', type=int, nargs='+',
                    help='The list of commands to send to the arduino separated by spaces ')
    parser.add_argument('--verbose', '-v', action='count', default=0)
    args = parser.parse_args()

    with open('config.yaml') as f:
        config = yaml.safe_load(f)

    send_cmd(args, config)