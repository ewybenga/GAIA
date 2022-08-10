#include <Wire.h>
#include <SoilMoistureSensor.h>
#include <WaterPump.h>
#include <LightSensor.h>

String command;
int seconds;

void setup() {
  Serial.begin(9600); // open the serial port and set the baud rate to 9600bps
  Wire.begin();
  digitalWrite(PIN_RELAY_1, HIGH);  // set default for pump to not pumping
  pinMode(PIN_RELAY_1, OUTPUT);  // initialize digital pin as an output.

}

void loop() {
  if (Serial.available()) {
    command = Serial.readStringUntil('\n'); // https://www.norwegiancreations.com/2017/12/arduino-tutorial-serial-inputs/#:~:text=Arduino%20serial%20monitor.-,Sending%20Commands,-A%20more%20usable

    if (command.equals("1")) { // Our encoding for "Send all data"
      Serial.print(sense_SM(A0)); // Send soil moisture percentage (probe 1)
      Serial.print(",");
      Serial.print(sense_SM(A1)); // Send soil moisture percentage (probe 2)
      Serial.print(",");
      Serial.print(sense_Light()); // Send light value (in lux)
      Serial.print(",");
    }
    else if (command.equals("2")) { // Our encoding for "Send soil moisture percentage"
      Serial.print(sense_SM(A0));
    }
    else if (command.equals("3")) { // Our encoding for "water the plant"
      Serial.print("watering, enter seconds");
      while(Serial.available() == 0) {
      }
      if (Serial.available()) {
        seconds = Serial.readStringUntil('\n').toInt();
        Serial.print(water(seconds));
      }
    }
    else if (command.equals("4")) { // Our encoding for "Send soil moisture percentage"
      Serial.print(sense_Light());
    }
  }
}
