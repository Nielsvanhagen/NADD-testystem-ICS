//main.cpp

#include <Arduino.h>
#include "sdTest.h"
#include "eepromTest.h"
#include "ioTest.h"
// #include "eeprom.h"

void setup() {
  Serial.begin(9600);
   while (!Serial) {
     ;}

     pinMode(PIN_GPI1, INPUT_PULLUP);
   	 pinMode(PIN_GPI2, INPUT_PULLUP);
   	 pinMode(PIN_GPI3, INPUT_PULLUP);

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
      ioTest();
    }
  }
}
