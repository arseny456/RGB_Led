#include "Parser.h"

#define DELAY_TICK 500

#define red_led 9
#define green_led 10
#define blue_led 11

void setup() {
  pinMode(red_led, OUTPUT);
  pinMode(green_led, OUTPUT);
  pinMode(blue_led, OUTPUT);
  Serial.begin(57600);
}


unsigned long senson_tick = 0;

void loop() { // run over and over
  if (Serial.available()) {
    char buf[20];
    Serial.readBytesUntil(";", buf, 20);
    Parser data(buf, ',');
    int ints[10];
    data.parseInts(ints);

    switch (ints[0]) {
      case 1:
        Serial.println("LED 1 to " + String(ints[1]));
        analogWrite(red_led, ints[1]);
        break;

      case 2:
        Serial.println("LED 2 to " + String(ints[1]));
        analogWrite(green_led, ints[1]);
        break;

      case 3:
        Serial.println("LED 3 to " + String(ints[1]));
        analogWrite(blue_led, ints[1]);
        break;
    }
  }

  if (millis() - senson_tick >= DELAY_TICK) {
    senson_tick = millis();
    int a = map(analogRead(A0), 0, 1023, 0, 255);
    Serial.println(a);
  }
}










