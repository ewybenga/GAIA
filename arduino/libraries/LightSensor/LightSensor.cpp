#include <BH1750.h>
#include "LightSensor.h"

BH1750 lightMeter(0x23);  // we are using 0x23 because we have connected the ADDR pin to ground


int sense_Light() { // Sense soil moisture
  lightMeter.begin();
  float lux = lightMeter.readLightLevel();
  return lux;
}
