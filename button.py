#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
from rpi_displays.sainsmart.displays import LCD2004

lcd = LCD2004()

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
button2 = 20
button3 = 26
button4 = 19
button5 = 6
button6 = 5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(all_relays, GPIO.OUT, initial=GPIO.HIGH)

def __init__():
    lcd.clear()
    lcd.display_string("CMC BH-30 Controller", 1)
    lcd.display_string("", 2)
    lcd.display_string("Ready...", 3)
    GPIO.add_event_detect(button1, GPIO.FALLING, callback=relayone, bouncetime=300)
    GPIO.add_event_detect(button2, GPIO.FALLING, callback=relaytwo, bouncetime=300)
    GPIO.add_event_detect(button3, GPIO.FALLING, callback=relaythree, bouncetime=300)
    GPIO.add_event_detect(button4, GPIO.FALLING, callback=relayfour, bouncetime=300)
    GPIO.add_event_detect(button5, GPIO.FALLING, callback=relayfive, bouncetime=300)
    GPIO.add_event_detect(button6, GPIO.FALLING, callback=relaysix, bouncetime=300)

def relayone(channel):
    if GPIO.input(relay1):
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay 1 was OFF", 3)
        lcd.display_string("Relay 1 now ON", 4)
        GPIO.output(all_relays, GPIO.HIGH)
        GPIO.output(relay1, GPIO.LOW)

    else:
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay 1 was ON", 3)
        lcd.display_string("Relay 1 now OFF", 4)
        GPIO.output(all_relays, GPIO.HIGH)

def relaytwo(channel):
    if GPIO.input(relay2):
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay 2 was OFF", 3)
        lcd.display_string("Relay 2 now ON", 4)
        GPIO.output(all_relays, GPIO.HIGH)
        GPIO.output(relay2, GPIO.LOW)

    else:
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay 2 was ON", 3)
        lcd.display_string("Relay 2 now OFF", 4)
        GPIO.output(all_relays, GPIO.HIGH)

def relaythree(channel):
    if GPIO.input(relay3):
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay 3 was OFF", 3)
        lcd.display_string("Relay 3 now ON", 4)
        GPIO.output(all_relays, GPIO.HIGH)
        GPIO.output(relay3, GPIO.LOW)

    else:
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay 3 was ON", 3)
        lcd.display_string("Relay 3 now OFF", 4)
        GPIO.output(all_relays, GPIO.HIGH)

def relayfour(channel):
    if GPIO.input(relay4):
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay 4 was OFF", 3)
        lcd.display_string("Relay 4 now ON", 4)
        GPIO.output(all_relays, GPIO.HIGH)
        GPIO.output(relay4, GPIO.LOW)

    else:
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay 4 was ON", 3)
        lcd.display_string("Relay 4 now OFF", 4)
        GPIO.output(all_relays, GPIO.HIGH)


def relayfive(channel):
    if GPIO.input(relay5):
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay 5 was OFF", 3)
        lcd.display_string("Relay 5 now ON", 4)
        GPIO.output(all_relays, GPIO.HIGH)
        GPIO.output(relay5, GPIO.LOW)

    else:
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay 5 was ON", 3)
        lcd.display_string("Relay 5 now OFF", 4)
        GPIO.output(all_relays, GPIO.HIGH)

def relaysix(channel):
    if GPIO.input(relay6):
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay 6 was OFF", 3)
        lcd.display_string("Relay 6 now ON", 4)
        GPIO.output(all_relays, GPIO.HIGH)
        GPIO.output(relay6, GPIO.LOW)

    else:
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay 6 was ON", 3)
        lcd.display_string("Relay 6 now OFF", 4)
        GPIO.output(all_relays, GPIO.HIGH)


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
    try:
        __init__()
        while(True):
            sleep(.5)
    except KeyboardInterrupt:
        destroy()
