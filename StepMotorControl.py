import RPi.GPIO as GPIO
import time

motorPins = (12, 16, 18, 22)
CCWStep = (0x01,0x02,0x04,0x08)
CWStep = (0x08,0x04,0x02,0x01)

def setup():
    GPIO.setmode(GPIO.BOARD)
    for pin in motorPins:
        GPIO.setup(pin, GPIO.OUT)

def rotate(ms):
    for j in range(4):
        for i in range(4):
            GPIO.output(motorPins[i], ((CCWStep[j] == 1<<i)) and GPIO.HIGH or GPIO.LOW)

        if(ms < 3):
            ms = 3
        time.sleep(ms*0.001)

def moveSteps(ms, steps):
    for i in range(steps):
        rotate(ms)


def loop():
    fullCircle = 0
    while True:
        moveSteps(3,512)
        fullCircle += 1
        print('Rotated {} full circles'.format(fullCircle))

def destroy():
    GPIO.cleanup()

if __name__ == '__main__': # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()