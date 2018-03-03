#include <Servo.h>
#include <stdio.h>
#include <stdlib.h>

Servo myservo;  // create servo object to control a servo
String readString;
int pos = 0;    // variable to store the servo position
String c;

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);
  pos = 90;
  myservo.write(pos);

}

void loop() {
  if (Serial.available()) {
    String str = Serial.readStringUntil('\n');
    Serial.println("HI I GOT ");
    Serial.println(str);
    Serial.println("END");
    char compass = str[0];
    int angle = (str[1]-'0')*10 + (str[2]-'0');
    Serial.println(compass);
    Serial.println(angle);
    
    if (compass == 'R') {
//      for (int i = 0; i <= angle ; i += 1) {
      pos = pos + 1;
      myservo.write(pos);
      delay(10);
      // }
    } else if (compass == 'L') {
      //for (int i = 0; i <= angle ; i += 1) {
      pos = pos - 1;
      myservo.write(pos);
      delay(10);
      //}
    }
  }

}

