#ifndef WATER_PUMP_H
#define WATER_PUMP_H

#include <Arduino.h>

#define PIN_RELAY_1  2 // the Arduino pin, which connects to the IN1 pin of relay module
#define PIN_RELAY_2  3 // the Arduino pin, which connects to the IN2 pin of relay module
#define PIN_RELAY_3  4 // the Arduino pin, which connects to the IN3 pin of relay module
#define PIN_RELAY_4  5 // the Arduino pin, which connects to the IN4 pin of relay module

int water(int seconds);

#endif