#include <Arduino.h>

#include <AccelStepper.h>

AccelStepper stepper(AccelStepper::DRIVER, 2, 5);

void setup() {
    Serial.begin(115200);

    stepper.setEnablePin(8);
    stepper.setPinsInverted(false, false, true);

    // Serial.println("enabled");
    stepper.enableOutputs();
    // while (true)
    //     ;

    stepper.setMaxSpeed(40);
    stepper.setSpeed(40);
    stepper.setAcceleration(40);
}

void loop() {
    stepper.moveTo(abs(stepper.currentPosition() - 100));
    Serial.println(stepper.targetPosition());
    stepper.enableOutputs();
    stepper.runToPosition();
    delay(1000);
}
