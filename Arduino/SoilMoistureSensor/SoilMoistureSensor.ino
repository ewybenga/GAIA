const int AirValue = 520;
const int WaterValue = 240;
int soilMoistureValue = 0;
int soilMoisturePct = 0;
bool debug = true;

void setup() {
  Serial.begin(9600); // open the serial port and set the baud rate to 9600bps
}

void loop() {
  sense_SM();

  if(debug){ // Print statements viewable on the Serial Monitor, to toggle, change `debug` to `true` or `false`
    Serial.println("----");
    Serial.print(String(soilMoistureValue) + " --- ");
    Serial.println(String(soilMoisturePct) + "%");
  }
  delay(5000);
}

void sense_SM(){ // Sense soil moisture
  soilMoistureValue = analogRead(A0);  //put Sensor insert into soil
  soilMoisturePct = map(soilMoistureValue, AirValue, WaterValue, 0, 100);
  
  if(soilMoisturePct > 100){ // For confusion's sake if it's higher than our calibration just call it 100%
    soilMoisturePct = 100;
  }
  else if(soilMoisturePct < 0){ // Similarly if the value is below 0% moisture just call it 0%
    soilMoisturePct = 0;
  }
}
