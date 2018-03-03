#include <Wire.h>
#include "rgb_lcd.h"
#include <stdlib.h>

rgb_lcd lcd;

boolean startTime = false;
int count = 0;

void setup() {
    // set up the LCD's number of columns and rows:
    lcd.begin(16, 2);
    Serial.begin(9600);
    
    lcd.setRGB( 255,  255, 255);
    pinMode(4, OUTPUT);
}

void loop() {
  lcd.clear();

  if (Serial.available()) {
    String str = Serial.readStringUntil('\n');
    Serial.println(str);
    char start = str[0];
    if (start == 'S') {
      for (int i = 0; i < 3; i++) {
        digitalWrite(4, HIGH);
        delay(500);
        digitalWrite(4, LOW);
        delay(500);        
      }

      startTime = true;
      count = 0;
    } else {
      startTime = false;
    }
  }
  
  if (startTime) {
    int r = rand() % 255 + 0;
    int g = rand() % 255 + 0;
    int b = rand() % 255 + 0;
    lcd.setRGB(r,g,b);
  
    int h = (count/3600); 
    int m = (count -(3600*h))/60;
    int s = (count -(3600*h)-(m*60));
    char* timer = (char*)malloc(12 * sizeof(char));
    sprintf(timer, "%d:%d:%d\n",h,m,s);
    lcd.print(timer);
    free(timer);
    count += 1;
  } else {
    lcd.print("Let's Start");
  }
  delay(1000);

}

