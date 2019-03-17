#include <SoftwareSerial.h>

SoftwareSerial EEBlue(10, 11); // RX | TX

int baud_at_cmd = 9600;

void setup() {  
  pinMode(9, OUTPUT);  // this pin will pull the HC-05 pin 34 (key pin) HIGH to switch module to AT mode
  digitalWrite(9, HIGH);
  Serial.begin(9600);
  EEBlue.begin(baud_at_cmd);  //Default Baud for comm, it may be different for your Module. 
  Serial.println("The bluetooth gates are open.\n Connect to HC-05 from any other bluetooth device with 1234 as pairing key!.");
}

void loop(){
  // Feed any data from bluetooth to Terminal.
  if (EEBlue.available()){
    Serial.write(EEBlue.read());
  }
 
  // Feed all data from terminal to bluetooth
  if (Serial.available()){
    EEBlue.write(Serial.read());
  }
}
