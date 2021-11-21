//======================================================================
// Controller code for a simple keyboard application
// Daniel Luoma, 2021
//======================================================================


int notes[] = {350, 330, 293, 261};

void setup() {
    Serial.begin(9600);
}

void loop() {
    int keyVal = analogRead(A0);
    Serial.println(keyVal);

    if(keyVal == 1023){
        tone(8, notes[0]);
    }

    else if(keyVal >= 990 && keyVal <= 1010){
        tone(8, notes[1]);
    }

    else if(keyVal >= 505 && keyVal <= 520){
        tone(8, notes[2]);
    }

    else if(keyVal >= 1 && keyVal <= 100){
        tone(8, notes[3]);
    }

    else {
        noTone(8);
    }
}
