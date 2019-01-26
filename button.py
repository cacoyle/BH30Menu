#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

all_relays = [11, 12, 13, 14, 15, 16, 17, 18]
num_relays = len(all_relays)

relay1 = 11
relay2 = 12
relay3 = 13
relay4 = 14
relay5 = 15
relay6 = 16
relay7 = 17
relay8 = 18
button1 = 21
button8 = 26

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(button8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(all_relays, GPIO.OUT, initial=GPIO.HIGH)

def one(channel):
    if GPIO.input(relay1):

        print("Relay 1 was OFF. Switching ON.")
        GPIO.output(all_relays, GPIO.HIGH)
        GPIO.output(relay1, GPIO.LOW)

    else:
        print("Relay 1 was ON. Switching OFF.")
        GPIO.output(all_relays, GPIO.HIGH)

def eight(channel):
    if GPIO.input(relay8):

        print("Relay 8 was OFF. Switching ON.")
        GPIO.output(all_relays, GPIO.HIGH)
        GPIO.output(relay8, GPIO.LOW)

    else:
        print("Relay 8 was ON. Switching OFF.")
        GPIO.output(all_relays, GPIO.HIGH)

def main():
    GPIO.add_event_detect(button1, GPIO.FALLING, callback=one, bouncetime=300)
    GPIO.add_event_detect(button8, GPIO.FALLING, callback=eight, bouncetime=300)

def destroy():
    GPIO.output(all_relays, GPIO.HIGH)
    sleep(0.5)
    GPIO.cleanup()
    print('\nQuitting.\n')

if __name__ == '__main__':
    setup()
    try:
        main()
        while(True):
            sleep(0.5)
    except KeyboardInterrupt:
        destroy()
