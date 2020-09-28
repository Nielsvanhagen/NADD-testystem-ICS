//main.cpp

#include <Arduino.h>
#include <EEPROM.h>
#include "sdTest.h"

uint8_t* addr = 0;
int val = 22;
void eepromTest();

void setup() {
  Serial.begin(9600);
   while (!Serial) {
     ;}
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
  }
  delay(1000);
}

void eepromTest(){
  Serial.println("Writing to eeprom...");
  eeprom_write_byte(addr, val);
  addr = 0;
  for(int i = 1; i < 100; i++ ){
      eeprom_write_byte(addr, i);
      //Serial.println(i);
      addr = addr + 1;
  }
  delay(500);
  Serial.println("Reading from eeprom...");

  addr = 0;
  for(int i = 0; i < 100; i++ ){
      byte value = eeprom_read_byte(addr);

      if(!(value == i)){
        Serial.println("EEPROM fault by byte: " + i);
      }
      //Serial.println(value);
      addr = addr + 1;
  }
  Serial.println("Erasing test files...");
  for ( unsigned int i = 0 ; i < EEPROM.length() ; i++ ){
    EEPROM.write(i, 0);
  }

}
