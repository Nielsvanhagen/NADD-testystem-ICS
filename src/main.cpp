#include <Arduino.h>
#include "sdTest.h"

void setup() {
  Serial.begin(9600);
   while (!Serial) {
     ;}
     
  //Serial.println("NADD test system version: 1.0");

  Serial.println("Starting sd card test...");
  sdCardTest(); //sd card function
}

void loop() {
  // put your main code here, to run repeatedly:
}
