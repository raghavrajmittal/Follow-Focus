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
    char compass = str[0];
    Serial.println(compass);
        
    if (compass == 'R') {
      pos = pos + 1;
      myservo.write(pos);
      delay(10);
     
    } else if (compass == 'L') {
      pos = pos - 1;
      myservo.write(pos);
      delay(10);
      
    }
  }
}

