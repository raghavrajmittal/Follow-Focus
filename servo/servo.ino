#include <Servo.h>
#include <stdio.h>
#include <stdlib.h>

Servo myservo;  // create servo object to control a servo

int pos = 0;    // variable to store the servo position

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);
  pos = myservo.read();
}

void loop() {
  
  if (Serial.available()) {
        String str = Serial.readString();
        char dir = str[0];
        int tim = (str[1]-'0')*10 + (str[2]-'0');
        Serial.println(dir);
        Serial.println(tim_str);

        if (dir == 'R') {
          for (int i = 0; i <= tim ; i += 1) {
            pos = pos + 1;
            myservo.write(pos);
            delay(10);
          }
       
        } else if (dir == 'L') {
          for (int i = 0; i <= tim ; i += 1) {
            pos = pos - 1;
            myservo.write(pos);
            delay(10);
          }
        }
        
  }
 
}

