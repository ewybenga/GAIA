#include "WaterPump.h"

void water(int seconds){
  digitalWrite(PIN_RELAY_1, LOW);  // Start pumping water

  delay(seconds * 1000);  // wait for <seconds> seconds
  
  digitalWrite(PIN_RELAY_1, HIGH);  // Stop pumping water
}