#include <SD.h>
#include <SPI.h>
#include "sdTest.h"

File myFile;

//Selection of the chip
const int chipSelect = BUILTIN_SDCARD;

//boolean for tests SD sdCard
bool initialized = false;
bool writeToSD = false;
bool readfromSD = false;

void sdCardTest(){
  Serial.println("Initializing SD card...");

  if (!SD.begin(chipSelect)) {
    Serial.println("ERROR initialization failed!");
    return;
  }
  Serial.println("Initialization done.");

  initialized = true;

  // open the file.
  myFile = SD.open("test.txt", FILE_WRITE);

  // if the file opened okay, write to it:
  if (myFile) {
    Serial.println("Writing to test.txt...");
    myFile.println("Test printline");

	// close the file:
    myFile.close();
    writeToSD = true;
  } else {
    // if the file didn't open, print an error:
    Serial.println("ERROR opening test.txt");
  }

  // re-open the file for reading:
  myFile = SD.open("test.txt");
  if (myFile) {
    // read from the file until there's nothing else in it:
    while (myFile.available()) {
    	Serial.write(myFile.read());
    }

    // close the file:
    myFile.close();

    readfromSD = true;
  } else {
  	// if the file didn't open, print an error:
    Serial.println("ERROR opening test.txt");
  }
  SD.remove("test.txt"); 
  // SD.remove("TEST.TXT");
  // if(! SD.remove("test.txt")){
  //   Serial.println(F("ultra not working"));
  //   return;
  // }
  //
  // if(initialized && writeToSD && readfromSD){
  //   Serial.println("SD TEST COMPLETE");
  // }
}