#ifndef __eepromTest_H__
#define __eepromTest_H__
#include <Arduino.h>
#include <EEPROM.h>

#define eeprom 0x50

extern uint8_t* addr;
extern int val;
extern boolean EEPROM_stat;

void eepromTest();

#endif
