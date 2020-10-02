#ifndef __sdTest_H__
#define __sdTest_H__
#include <Arduino.h>

//Selection of the chip
extern const int chipSelect;

//boolean for tests SD sdCard
extern bool fault_initialized;
extern bool fault_formatSD;
extern bool fault_writeToSD;
extern bool fault_readfromSD;

void sdCardTest();

#endif
