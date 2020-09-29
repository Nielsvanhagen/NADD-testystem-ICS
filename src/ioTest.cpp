#include "ioTest.h"

void ioTest(){
  Serial.println("test!");
  digitalWrite(PIN_GPO1,HIGH);
  delay(500);
  digitalWrite(PIN_GPO1,LOW);
  Serial.println("T3-t");
}
