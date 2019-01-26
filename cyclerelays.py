#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

all_relays = [11, 12, 13, 14, 15, 16, 17, 18]
num_relays = len(all_relays)

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(all_relays, GPIO.OUT, initial=GPIO.HIGH)

def main():


    while True:

        for i in range(0, num_relays, +1):
            GPIO.output(all_relays[i], GPIO.LOW)
            sleep(0.5)
            GPIO.output(all_relays[i], GPIO.HIGH)
            sleep(0.5)

def destroy():
    GPIO.output(all_relays, GPIO.HIGH)
    GPIO.cleanup()
    print("\nQuitting.\n")

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
