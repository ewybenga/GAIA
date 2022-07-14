 #include "src/SoilMoistureSensor.h" // the file that hold the function sense_SM (sense soil moisture)
 #include "src/WaterPump.h" // the file that hold the function sense_SM (sense soil moisture)

String command;

void setup() {
  Serial.begin(9600); // open the serial port and set the baud rate to 9600bps

  pinMode(PIN_RELAY_1, OUTPUT);  // initialize digital pin as an output.
  digitalWrite(PIN_RELAY_1, HIGH);  // set default for pump to not pumping
}

void loop() {
  if (Serial.available()) {
    command = Serial.readStringUntil('\n'); // https://www.norwegiancreations.com/2017/12/arduino-tutorial-serial-inputs/#:~:text=Arduino%20serial%20monitor.-,Sending%20Commands,-A%20more%20usable

    if (command.equals("1")) { // Our encoding for "Send all data"
      Serial.print(sense_SM()); // Send soil moisture percentage
      Serial.print(",");
    }
    else if (command.equals("2")) { // Our encoding for "Send soil moisture percentage"
      Serial.print(sense_SM());
    }
    else if (command.equals("3")) { // Our encoding for "Send soil moisture percentage"
      water(1);
    }
  }
}
