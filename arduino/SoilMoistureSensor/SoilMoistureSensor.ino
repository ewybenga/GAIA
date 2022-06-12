const int AirValue = 520;
const int WaterValue = 240;
int soilMoistureValue = 0;
int soilMoisturePct = 0;
String command;

void setup() {
  Serial.begin(9600); // open the serial port and set the baud rate to 9600bps
}

void loop() {
  if (Serial.available()) {
    command = Serial.readStringUntil('\n'); // https://www.norwegiancreations.com/2017/12/arduino-tutorial-serial-inputs/#:~:text=Arduino%20serial%20monitor.-,Sending%20Commands,-A%20more%20usable
    Serial.println(command);
    if (command.equals("1")) { // Our encoding for "Send all data"
      Serial.print(sense_SM()); // Send soil moisture percentage
      Serial.print(",");
    }
    else if (command.equals("2")) { // Our encoding for "Send soil moisture percentage"
      Serial.print(sense_SM());
    }
  }
}

int sense_SM() { // Sense soil moisture
  soilMoistureValue = analogRead(A0);  //put Sensor insert into soil
  soilMoisturePct = map(soilMoistureValue, AirValue, WaterValue, 0, 100);

  if (soilMoisturePct > 100) { // For confusion's sake if it's higher than our calibration just call it 100%
    soilMoisturePct = 100;
  }
  else if (soilMoisturePct < 0) { // Similarly if the value is below 0% moisture just call it 0%
    soilMoisturePct = 0;
  }

  return soilMoisturePct;
}
