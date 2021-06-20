#include <Arduino.h>

#include "HX711.h"

const int LOADCELL_DOUT_PIN = 2;
const int LOADCELL_SCK_PIN = 3;

HX711 scale;

void setup() {
    Serial.begin(115200);

    scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
    scale.tare();
}

unsigned long start;
void loop() {
    if (scale.is_ready()) {
        auto value = scale.read();

        unsigned long end = millis();
        unsigned long elapsed = end - start;
        start = millis();

        Serial.println(value);
        // Serial.print(" ");
        // Serial.println(elapsed);
    }
}
