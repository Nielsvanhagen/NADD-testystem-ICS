//main.cpp

#include <Arduino.h>
#include "sdTest.h"
#include "eepromTest.h"
#include "ioTest.h"
// #include "eeprom.h"

void eepromTest();
#define PIN_GPO1	14				//light in push to talk button
#define PIN_GPO2	39				//TBD
#define PIN_GPO3	36				//TBD

void setup() {
  Serial.begin(9600);
   while (!Serial) {
     ;}

     pinMode(PIN_GPO1, OUTPUT);
     pinMode(PIN_GPO2, OUTPUT);
     pinMode(PIN_GPO3, OUTPUT);
  //Serial.println("NADD test system version: 1.0");
}

void loop() {
  if (Serial.available()>0) {
    char serIn=Serial.read();
    if (serIn=='1') {
      delay(500);
      Serial.println("Starting sd card test...");
      sdCardTest(); //sd card function
    }
    else if(serIn=='2') {
      delay(500);
      Serial.println("Starting eeprom test...");
      eepromTest();
    }
    else if(serIn=='3') {
      delay(500);
      Serial.println("Starting IO test...");
      digitalWrite(PIN_GPO1, HIGH);
      delay(500);
      digitalWrite(PIN_GPO1, LOW);
      ioTest();
    }
  }
}
