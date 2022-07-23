#include "SoilMoistureSensor.h"

const int AirValue1 = 462;
const int WaterValue1 = 201;

const int AirValue2 = 494;
const int WaterValue2 = 237;
int soilMoistureValue = 0;
int soilMoisturePct = 0;


int sense_SM(uint8_t pin) { // Sense soil moisture
  soilMoistureValue = analogRead(pin);  //put Sensor insert into soil
  if (pin == 14){ //pin 14 is calibrated to air/water val 1
    soilMoisturePct = map(soilMoistureValue, AirValue1, WaterValue1, 0, 100);
  }
  else if (pin == 15){ //pin 15 is calibrated to air/water val 2
    soilMoisturePct = map(soilMoistureValue, AirValue2, WaterValue2, 0, 100);
  }

  if (soilMoisturePct > 100) { // For confusion's sake if it's higher than our calibration just call it 100%
    soilMoisturePct = 100;
  }
  else if (soilMoisturePct < 0) { // Similarly if the value is below 0% moisture just call it 0%
    soilMoisturePct = 0;
  }

  return soilMoisturePct;
}
