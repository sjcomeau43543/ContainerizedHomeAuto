#include <Wire.h>
#include <Adafruit_AMG88xx.h>
#include "SoftwareSerial.h"

SoftwareSerial EEBlue(10, 11); // RX | TX

Adafruit_AMG88xx amg;

float pixels[AMG88xx_PIXEL_ARRAY_SIZE];

int count = 0;
bool lastTickPositiveSide = false;
bool lastTickNegativeSide = false;
int humanTempCutoff = 25;

void setup() {
    Serial.begin(9600);
    EEBlue.begin(9600);
    Serial.println(F("AMG88xx pixels"));

    bool status;
    
    // default settings
    status = amg.begin();
    if (!status) {
        Serial.println("Could not find a valid AMG88xx sensor, check wiring!");
        while (1);
    }
    
    Serial.println("-- Pixels Test --");

    delay(100); // let sensor boot up
}


void loop() { 
    //read all the pixels
    amg.readPixels(pixels);

    bool positiveSide = false;
    bool negativeSide = false;
    Serial.print("[");
    for(int i=1; i<=AMG88xx_PIXEL_ARRAY_SIZE; i++){
      if (pixels[i-1] > humanTempCutoff) {
        Serial.print("XXX");
        if( i%8 == 0 || (i+1)%8 == 0 || (i+2)%8 == 0 || (i+3)%8 == 0 ) // "positive" side
          positiveSide = true;
        if( (i+4)%8 == 0 || (i+5)%8 == 0 || (i+6)%8 == 0 || (i+7)%8 == 0 ) // "positive" side
          negativeSide = true;
      }
      else Serial.print("   ");
      if( i%8 == 0 ) Serial.print("|\n|");
    }
    Serial.println("]");
    Serial.println();

    // if they're all the same, don't bother
    if (!((lastTickNegativeSide && lastTickPositiveSide && positiveSide && negativeSide) ||
          (!lastTickNegativeSide && !lastTickPositiveSide && !positiveSide && !negativeSide))) {
      if (lastTickNegativeSide && positiveSide) 
        moveNegativeToPositive();
      if (lastTickPositiveSide && negativeSide)
        movePositiveToNegative();
      lastTickPositiveSide = positiveSide;
      lastTickNegativeSide = negativeSide;
   }

    char buff[30];
    sprintf(buff, "Positive Side: %d", lastTickPositiveSide);
    Serial.println(buff);
    sprintf(buff, "negative Side: %d", lastTickNegativeSide);
    Serial.println(buff);

    sprintf(buff, "There are %i people in the room.", count);
    Serial.println(buff);
    
    //delay a second
    delay(100);
  }

  void moveNegativeToPositive() {
    count ++;
    char buff[30];
    sprintf(buff, "There are %i people in the room.\n", count);
    EEBlue.write(buff);
    Serial.print(buff);
  }
  void movePositiveToNegative() {
    count --;
    char buff[30];
    sprintf(buff, "There are %i people in the room.\n", count);
    EEBlue.write(buff);
    Serial.print(buff);
  }
