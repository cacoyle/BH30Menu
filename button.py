#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
from rpi_displays.sainsmart.displays import LCD2004

lcd = LCD2004()

lcd.clear()
lcd.display_string("CMC BH-30 Controller", 1)
lcd.display_string("", 2)
lcd.display_string("Ready...", 3)
#lcd.display_string("12345678901234567890", 4)

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
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay 1 was OFF", 3)
        lcd.display_string("Switching ON", 4)
        GPIO.output(all_relays, GPIO.HIGH)
        GPIO.output(relay1, GPIO.LOW)

    else:
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay 1 was ON", 3)
        lcd.display_string("Switching OFF", 4)
        GPIO.output(all_relays, GPIO.HIGH)

def eight(channel):
    if GPIO.input(relay8):
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay 8 was OFF", 3)
        lcd.display_string("Switching ON", 4)
        GPIO.output(all_relays, GPIO.HIGH)
        GPIO.output(relay8, GPIO.LOW)

    else:
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay 8 was ON", 3)
        lcd.display_string("Switching OFF", 4)
        GPIO.output(all_relays, GPIO.HIGH)

def main():
    GPIO.add_event_detect(button1, GPIO.FALLING, callback=one, bouncetime=300)
    GPIO.add_event_detect(button8, GPIO.FALLING, callback=eight, bouncetime=300)

def destroy():
    lcd.clear()
    lcd.display_string("CMC BH-30 Controller", 1)
    lcd.display_string("Goodbye.", 3)
    GPIO.output(all_relays, GPIO.HIGH)
    sleep(2)
    GPIO.cleanup()
    lcd.clear()
    lcd.switch_backlight(0)

if __name__ == '__main__':
    setup()
    try:
        main()
        while(True):
            sleep(0.5)
    except KeyboardInterrupt:
        destroy()
