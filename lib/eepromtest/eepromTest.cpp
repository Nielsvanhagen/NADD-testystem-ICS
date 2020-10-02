#include "eepromTest.h"
#include <Wire.h>

uint8_t* addr = 0;
int val = 1;
boolean EEPROM_stat = true;

void eepromTest(){
  eeprom_write_byte(addr, val);
  addr = 0;
  for(int i = 0; i < 100; i++ ){
      eeprom_write_byte(addr, i);
      //Serial.println(i);
      addr = addr + 1;
}
delay(500);
Serial.println("Reading from eeprom...");

addr = 0;
for(int i = 0; i < 100; i++ ){
    byte value = eeprom_read_byte(addr);
    //Serial.println(value);

    if(!(value == i)){
      EEPROM_stat = false;
    }
    //Serial.println(value);
    addr = addr + 1;
}
Serial.println("Erasing test files...");
for ( unsigned int i = 0 ; i < EEPROM.length() ; i++ ){
    EEPROM.write(i, 0);
}

if(EEPROM_stat){
  Serial.println("EEPROM test complete!...");
  Serial.println("T2-t");
}
else{
  Serial.println("EEPROM test not complete");
  Serial.println("T2-f");
}
}
