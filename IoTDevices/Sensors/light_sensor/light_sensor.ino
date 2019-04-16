#include <SoftwareSerial.h>
SoftwareSerial EEBlue(10, 11); // RX | TX

int sensorPin = A0;    // select the input pin for the potentiometer
int sensorValue = 0;  // variable to store the value coming from the sensor

const int numReadings = 10;
const int lightCutoffVal = 30;

int readings[numReadings];      // the readings from the analog input
int readIndex = 0;              // the index of the current reading
int total = 0;                  // the running total
int average = 0;                // the average

int lastAverage = 0;

void setup() {
  Serial.begin(9600);
  EEBlue.begin(9600);
  
  for (int thisReading = 0; thisReading < numReadings; thisReading++) {
    readings[thisReading] = 0;
  }
}

void loop() {
  // subtract the last reading:
  total = total - readings[readIndex];
  // read from the sensor:
  readings[readIndex] = analogRead(sensorPin);
  // add the reading to the total:
  total = total + readings[readIndex];
  // advance to the next position in the array:
  readIndex = readIndex + 1;

  // if we're at the end of the array...
  if (readIndex >= numReadings) {
    // ...wrap around to the beginning:
    readIndex = 0;
  }

  lastAverage = average;
  // calculate the average:
  average = total / numReadings;
  
  // send it to the computer as ASCII digits
  Serial.println(average);
  if (average > lightCutoffVal && lastAverage <= lightCutoffVal) {
    EEBlue.write("1");
  }
  else if (average < lightCutoffVal && lastAverage >= lightCutoffVal) {
    EEBlue.write("0");
  }
  
  delay(500);
}
