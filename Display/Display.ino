#include <Wire.h>
#include "rgb_lcd.h"

rgb_lcd lcd;

boolean startTime = false;
String mainText = "Let's Start";
int count = 0;
void setup() {
    // set up the LCD's number of columns and rows:
    lcd.begin(16, 2);
    Serial.begin(9600);
    lcd.setRGB( 255,  255, 255);
}

void loop() {
  lcd.clear();
  if (Serial.available()) {
    String str = Serial.readStringUntil('\n');
    Serial.println(str);
    char start = str[0];
    if (start == 'S') {
      startTime = true;
      count = 0;
    } else {
      startTime = false;
    }
  }
  
  if (startTime) {
    lcd.print(count);
    count += 1;
  } else {
    lcd.print("nanana");
  }
  delay(1000);

}

