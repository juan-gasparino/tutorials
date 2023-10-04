#include <Arduino.h>

int const PIN_BUTTON = 2;
int const PIN_LED = 3;
int const TIME_DELAY = 5000;
int status = LOW;

void setup() {
    // put your setup code here, to run once:
    pinMode(PIN_BUTTON, INPUT);
    pinMode(PIN_LED, OUTPUT);
}

void loop() {
    // put your main code here, to run repeatedly:
    while (digitalRead(PIN_BUTTON) == LOW) {} //wait button is push
    status = digitalRead(PIN_LED);
    delay(TIME_DELAY);
    digitalWrite(PIN_LED, !status);
    while (digitalRead(PIN_BUTTON) == HIGH) {} //avoid overpush
}