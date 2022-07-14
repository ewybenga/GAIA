#include "SoilMoistureSensor.h"

const int AirValue = 520;
const int WaterValue = 240;
int soilMoistureValue = 0;
int soilMoisturePct = 0;


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
