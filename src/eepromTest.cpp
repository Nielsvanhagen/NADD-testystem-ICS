#include "eepromTest.h"
#include <Wire.h>
#define eeprom 0x50

uint8_t* addr = 0;
int val = 1;
boolean EEPROM_stat = true;

// void writeEEPROM(int deviceaddress, unsigned int eeaddress, byte data ) {
// Wire.beginTransmission(deviceaddress);
// Wire.write((int)(eeaddress >> 8));      //writes the MSB
// Wire.write((int)(eeaddress & 0xFF));    //writes the LSB
// Wire.write(data);
// Wire.endTransmission();
// }
//
// //defines the readEEPROM function
// byte readEEPROM(int deviceaddress, unsigned int eeaddress ) {
// byte rdata = 0xFF;
// Wire.beginTransmission(deviceaddress);
// Wire.write((int)(eeaddress >> 8));      //writes the MSB
// Wire.write((int)(eeaddress & 0xFF));    //writes the LSB
// Wire.endTransmission();
// Wire.requestFrom(deviceaddress,1);
// if (Wire.available())
//   rdata = Wire.read();
// return rdata;
// }
//
//   void eepromTest(){
//
//   Wire.begin(); //creates a Wire object
//   Serial.begin(9600);
//
//   unsigned int address = 0; //first address of the EEPROM
//   Serial.println("We write the zip code 22222, a zip code");
//   for(address = 0; address< 5; address++)
//     writeEEPROM(eeprom, address, '2'); // Writes 22222 to the EEPROM
//
//   for(address = 0; address< 5; address++) {
//     Serial.print(readEEPROM(eeprom, address), HEX);
//     }
//     }



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
