#include <SoftwareSerial.h>

SoftwareSerial EEBlue(10, 11); // RX | TX
int EEBlue_data;
int Serial_data;

int motorPin = 9;

void setup() {
  Serial.begin(9600);
  EEBlue.begin(9600);  //Default Baud for comm, it may be different for your Module. 
  Serial.println("The bluetooth gates are open.\n Connect to HC-05 from any other bluetooth device with 1234 as pairing key!.");

  pinMode(motorPin, OUTPUT);
}

void loop(){
  // Feed any data from bluetooth to Terminal.
  if (EEBlue.available()){
    EEBlue_data = EEBlue.read();
    Serial.write(EEBlue_data);
    
    if (EEBlue_data == '0'){
      EEBlue.println("SUCCESS : Turning the fan off");
      digitalWrite(motorPin, LOW);
    } else if (EEBlue_data == '1'){
      EEBlue.println("SUCCESS : Turning the fan on");
      digitalWrite(motorPin, HIGH);
    }
  }
 
  // Feed all data from terminal to bluetooth
  if (Serial.available()){
    Serial_data = Serial.read();
    EEBlue.write(Serial_data);
  }
}
