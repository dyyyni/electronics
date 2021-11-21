//======================================================================
// Controller code for a simple motor application
// Daniel Luoma, 2021
//======================================================================

const int switchPin = 2;
const int motorPin = 9;
int switchState = 0;

int potVal;
int const potPin = A0;
int motorPower;


void setup() {
  Serial.begin(9600);
  pinMode(motorPin, OUTPUT);
  pinMode(switchPin, INPUT);
}

void loop() {
  switchState = digitalRead(switchPin);
  potVal = analogRead(potPin);
  Serial.println(potVal);

  motorPower = map(potVal, 0, 1023, 0, 255);
  
  if (switchState == HIGH) {
    analogWrite(motorPin, motorPower);
    }
  else {
    digitalWrite(motorPin, LOW);
    }
}
