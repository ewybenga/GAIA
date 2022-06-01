# https://pyserial.readthedocs.io/en/latest/shortintro.html
# https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0#:~:text=check%20your%20installation.-,Step%203%3A%20Python%20Code,-First%20up%2C%20we

import serial
import time

def main():
    num = input("Enter a number: ") # Taking input from user
    arduino.write(bytes(num, 'utf-8'))
    time.sleep(0.05)
    for i in range(5):
        data = arduino.readline()
        if data==b'':
            break
        print(data)


if __name__ == "__main__":
    arduino = serial.Serial('COM3', 9600, timeout=1)
    main()