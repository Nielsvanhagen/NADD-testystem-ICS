#include <SD.h>
#include <SPI.h>
#include "sdTest.h"

File myFile;
//Selection of the chipSSSSSS
const int chipSelect = BUILTIN_SDCARD;

//boolean for tests SD sdCard
bool fault_initialized = false;
bool fault_formatSD = false;
bool fault_writeToSD = false;
bool fault_readfromSD = false;

Sd2Card card;
SdVolume volume;

void sdCardTest(){
  Serial.println("Initializing SD card...");

  if (SD.begin(chipSelect)) {
    Serial.println("Initialization done.");

    fault_initialized = true;
  }
  else{
    Serial.println("ERROR initialization failed!");
  }

  // if (!volume.init(card)) {
  //   Serial.println("Could not find FAT16/FAT32 partition.\nMake sure you've formatted the card");
  // }
  // else{
  //   fault_formatSD = true;
  // }
  // open the file.
  myFile = SD.open("test.txt", FILE_WRITE);

  // if the file opened okay, write to it:
  if (myFile) {
    Serial.println("Writing to test.txt...");
    myFile.println("Test printline");

	// close the file:
    myFile.close();
    fault_writeToSD = true;
  } else {
    // if the file didn't open, print an error:
    Serial.println("ERROR opening test.txt");
  }

  // re-open the file for reading:
  myFile = SD.open("test.txt");

  if (myFile){
    // read from the file until there's nothing else in it:
    while (myFile.available()) {
    	Serial.write(myFile.read());
    }

    // close the file:
    myFile.close();

    fault_readfromSD = true;
  } else {
  	// if the file didn't open, print an error:
    Serial.println("ERROR reading test.txt");
  }
  SD.remove("test.txt");

  //ACK command to tool
  if(fault_initialized && fault_writeToSD && fault_readfromSD){
    Serial.println("T1-t");
  }
  else{
    Serial.println("T1-f");
  }
}
