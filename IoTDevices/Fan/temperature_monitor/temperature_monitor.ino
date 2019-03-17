#include <SoftwareSerial.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>

SoftwareSerial EEBlue(10, 11); // RX | TX
int EEBlue_data;
int Serial_data;

int sensorPin = 9;
DHT dht(sensorPin, DHT22);
float humidity;
float temperature;

void setup() {
  Serial.begin(9600);
  EEBlue.begin(9600);  //Default Baud for comm, it may be different for your Module. 
  Serial.println("The bluetooth gates are open.\n Connect to HC-05 from any other bluetooth device with 1234 as pairing key!.");

  dht.begin();
  //pinMode(sensorPin, INPUT);
}

void loop(){
  // Read the temperature from the sensor
  delay(2000);
  humidity = dht.readHumidity();
  temperature = dht.readTemperature();
  
  Serial.print("Humidity:");
  Serial.print(humidity);
  Serial.println("%");
  Serial.print("Temperature:");
  Serial.print(temperature);
  Serial.print("degrees Celsius, ");
  Serial.print(temperature * 9 / 5 + 32);
  Serial.println("degrees Farenheit");
  delay(10000);
  
  // Feed any data from bluetooth to Terminal.
  if (EEBlue.available()){
    EEBlue_data = EEBlue.read();
    Serial.write(EEBlue_data);
  }
 
  // Feed all data from terminal to bluetooth
  if (Serial.available()){
    Serial_data = Serial.read();
    EEBlue.write(Serial_data);
  }
}
