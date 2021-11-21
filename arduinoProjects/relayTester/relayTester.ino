//======================================================================
// Controller code for a simple  application
// Daniel Luoma, 2021
//======================================================================

const int controlPin = 12;

void setup() {
pinMode(controlPin, OUTPUT);
}

void loop() {
  digitalWrite(controlPin, HIGH);
  delay(5000);
  digitalWrite(controlPin, LOW);
  delay(5000);
}
