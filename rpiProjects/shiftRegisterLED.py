'''
This python program uses a 74HC595 shift register to control 8 LEDs.
'''

import RPi.GPIO as GPIO
import time

LSBFIRST = 1
MSBFIRST = 2

# Pins for the 74HC595
dataPin = 11    # Serial data input
latchPin = 13   # Parallel data output
clockPin = 15   # Serial shift clock

def setup():
    GPIO.setmode(GPIO.BOARD) # Uses Physical GPIO numbering
    GPIO.setup(dataPin, GPIO.OUT) # set pin to output mode
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)

def shiftOut(dPin, cPin, order, val):
    for i in range(0,8):
        GPIO.output(cPin, GPIO.LOW)
        if(order == LSBFIRST):
            GPIO.output(dPin, (0x01&(val>>i)==0x01) and GPIO.HIGH or GPIO.LOW)
        elif(order == MSBFIRST):
            GPIO.output(dPin, (0x80&(val<<i)==0x80) and GPIO.HIGH or GPIO.LOW)

        GPIO.output(cPin, GPIO.HIGH)

def main():
    # Count from 0 to 255 and display in binary
    while True:
     for i in range(257):
         # ST_CP LOW to keep LEDs from changing while reading serial data
         GPIO.output(latchPin, GPIO.LOW)
         shiftOut(dataPin, clockPin, LSBFIRST, i)
         GPIO.output(latchPin, GPIO.HIGH)
         time.sleep(0.1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    print('Entering the program..')
    setup()
    try:
        main()
    except KeyboardInterrupt:
        print('Program ended by the user')
        destroy()
