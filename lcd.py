#!/usr/bin/python3
import RPi.GPIO as GPIO
from rpi_displays.sainsmart.displays import LCD2004
from time import sleep

lcd = LCD2004()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

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
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
lcd.clear()


def setup():
    lcd.display_string("CMC BH-30 Controller", 1)
    lcd.display_string("           by VA3DXV", 2)
    lcd.display_string("Ready...", 4)

def destroy():
    lcd.clear()
    lcd.display_string("CMC BH-30 Controller", 1)
    lcd.display_string("           by VA3DXV", 2)
    lcd.display_string("Goodbye...", 4)
    sleep(2)
    lcd.clear()
    exit()

def menu():
    lcd.clear()
    lcd.display_string("CMC BH-30 Controller", 1)
    lcd.display_string("Menu", 2)

def main():
    GPIO.add_event_detect(button1, GPIO.FALLING, callback=menu(0), bouncetime=300)
    GPIO.add_event_detect(button8, GPIO.FALLING, callback=main(0), bouncetime=300)

if __name__ == "__main__":
    setup()
    try:
        main()
        while(True):
            sleep(.2)
    except KeyboardInterrupt:
        destroy()

#if __name__ == '__menu__':
#    setup()
#
#    try:
#        menu()
#
#        while(True):
#            sleep(0.5)
#
#    except KeyboardInterrupt:
#        destroy()
