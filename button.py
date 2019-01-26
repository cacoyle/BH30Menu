#!/usr/bin/python
import RPi.GPIO as GPIO
import time

all_relays = [11, 12, 13, 14, 15, 16, 17, 18]
relay1 = 11
relay2 = 12
relay3 = 13
relay4 = 14
relay5 = 15
relay6 = 16
relay7 = 17
relay8 = 18
button_up = 21
button_dn = 26

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button_up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(button_dn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(all_relays, GPIO.OUT, initial=GPIO.HIGH)

def up(channel):
    print("Up button pressed.")
    if GPIO.input(18):
        print("Relay 8 was OFF. Switching ON.")
        GPIO.output(relay8, GPIO.LOW)
    else:
        print("Relay 8 was ON. Switching OFF.")
        GPIO.output(relay8, GPIO.HIGH)

def down(channel):
    print("Down button pressed.")
    if GPIO.input(11):
        print("Relay 1 was OFF. Switching ON.")
        GPIO.output(relay1, GPIO.LOW)
    else:
        print("Relay 1 was ON. Switching OFF.")
        GPIO.output(relay1, GPIO.HIGH)

def main():
    GPIO.add_event_detect(button_up, GPIO.FALLING, callback=up)
    GPIO.add_event_detect(button_dn, GPIO.FALLING, callback=down)

def destroy():
    GPIO.output(all_relays, GPIO.HIGH)
    GPIO.cleanup()
    print('\nQuitting.\n')

if __name__ == '__main__':
    setup()

    try:
        main()
        while(True):
            time.sleep(0.1)

    except KeyboardInterrupt:
        destroy()
