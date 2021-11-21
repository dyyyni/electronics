//======================================================================
// Controller code for a simple light theremin application
// Daniel Luoma, 2021
//======================================================================

// Variables to hold and map the sensor value
// Low and high are used for initialization and are calibrated
// as the program starts
int sensorValue;
int sensorLow = 1023;
int sensorHigh = 0;

const int ledPin = 13; // Uses the on-board LED

void setup(){

pinMode(ledPin, OUTPUT);
digitalWrite(ledPin, HIGH);

// Sensor calibration
while (millis() < 5000){
  sensorValue = analogRead(A0);
  if (sensorValue > sensorHigh) {
    sensorHigh = sensorValue;
  }
  if (sensorValue < sensorLow) {
    sensorLow = sensorValue;
  }
 }
digitalWrite(ledPin, LOW);
}

void loop() {
sensorValue = analogRead(A0);
int pitch = map(sensorValue, sensorLow, sensorHigh, 50, 4000);

tone(8, pitch, 20);

delay(10);
}
