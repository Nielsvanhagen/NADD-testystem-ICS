#include "ioTest.h"

bool fault_IO = true;

void ioTest(){
  //IO 1
  digitalWrite(PIN_GPO1, HIGH);
  delay(1000);
  if(digitalRead(PIN_GPI1)==0){
    Serial.println("IO 1 test complete!");
  }
  else{
    Serial.println("IO 1 test not complete!");
    fault_IO = false;
  }

  //IO2
  digitalWrite(PIN_GPO2, HIGH);
  delay(1000);
  if(digitalRead(PIN_GPI2)==0){;
    Serial.println("IO 2 test complete!");
  }
  else{
    Serial.println("IO 2 test not complete!");
    fault_IO = false;
  }

  //IO3
  digitalWrite(PIN_GPO3, HIGH);
  delay(1000);
  if(digitalRead(PIN_GPI3)==0){
    Serial.println("IO 3 test complete!");
  }
  else{
    Serial.println("IO 3 test not complete!");
    fault_IO = false;
  }
  //Serial.println(fault_IO);
  digitalWrite(PIN_GPO1, LOW);
  digitalWrite(PIN_GPO2, LOW);
  digitalWrite(PIN_GPO3, LOW);
  if(fault_IO){
    Serial.println("T3-t");
  }
  else{
    Serial.println("T3-f");
  }
}
