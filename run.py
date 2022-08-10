import argparse
import pandas as pd
import yaml
import sqlite3
from sqlite3 import Error
from src.arduino_comm import send_cmd
from src.sql_comm import create_connection, create_table, clean_data, insert_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Request data from the plant monitor.')
    parser.add_argument('commands', type=int, nargs='+',
                    help='The list of commands to send to the arduino separated by spaces ')
    parser.add_argument('--clean', '-c', action="store_true")
    parser.add_argument('--mitigate', '-m', action="store_true")
    parser.add_argument('--verbose', '-v', action='count', default=0)
    args = parser.parse_args()

    with open('config.yaml') as f:
        config = yaml.safe_load(f)

    data = send_cmd(args, config['port'], config['command_map'])

    conn = create_connection(config["db_path"])
    create_table(conn, config["table"], args.clean)
    insert_data(conn, config["table"], data )

    if args.mitigate and int(data[0]) <35:
        args.commands=[3,10]
        send_cmd(args, config['port'], config['command_map'])

    