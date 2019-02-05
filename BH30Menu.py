#!/usr/bin/python3
# BH30Menu.py
# 29/01/2019
#
# Copyright 2019 - Brian Graves - VA3DXV
#
# va3dxv@gmail.com
#
# https://github.com/va3dxv
#
#   This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#############################################################################
import RPi.GPIO as GPIO
import datetime
import pytz
import requests
import argparse
import xmltodict
import socket
from time import sleep
from rpi_displays.sainsmart.displays import LCD2004

progName="CMC BH-30 Controller"
readyMsg="Ready...      VA3DXV"

lcd=LCD2004()

parser = argparse.ArgumentParser()
parser.add_argument("-cli", help="Enable CLI menu.", action="store_true", default=False)
args = parser.parse_args()

relayBounceTime = 500

relayPins={
    11: {
        "button": 21,
        "band": "80M Low",
        "spotband": "80"
    },
    12: {
        "button": 20,
        "band": "80M High",
        "spotband": "80"
    },
    13: {
        "button": 26,
        "band": "40M Low",
        "spotband": "40"
    },
    14: {
        "button": 19,
        "band": "40M High",
        "spotband": "40"
    },
    15: {
        "button": 6,
        "band": "20M Low",
        "spotband": "20"
    },
    16: {
        "button": 5,
        "band": "20M High",
        "spotband": "20"
    },
    17: {
        "button": 25,
        "band": "15M",
        "spotband": "15"
    },
    18: {
        "button": 24,
        "band": "10M",
        "spotband": "10"
    }
}
allRelays = list(relayPins.keys())

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(allRelays, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(
    [relayPins[x]["button"] for x in relayPins],
    GPIO.IN,
    pull_up_down=GPIO.PUD_UP
)

def __init__():
    lcd.clear()
    lcd.display_string(progName, 1)
    lcd.display_string(readyMsg, 4)
    for relay in relayPins:
        GPIO.add_event_detect(
            relay["button"],
            GPIO.FALLING,
            callback=relayPress(relayNum=relay),
            bouncetime=relayBounceTime
        )

def tuning(band):
    print("\nTuning to " + band + ".\n")
    print("Wait for BH-30...\n")
    lcd.clear()
    lcd.display_string(progName, 1)
    lcd.display_string("Tuning to " + band, 2)
    lcd.display_string("Wait for BH-30...", 4)
    sleep(5)

def tuned(band):
    print("Tuned to " + band + "\n")
    lcd.clear()
    lcd.display_string(progName, 1)
    lcd.display_string("Tuned to " + band, 2)
    lcd.display_string(readyMsg, 4)

def alreadyTuned(band):
    print("\n" + band + " is already selected!\n")
    print("Getting DX spots...\n")
    lcd.clear()
    lcd.display_string(progName, 1)
    lcd.display_string("Already on " + band, 3)
    lcd.display_string("Getting DX spots...", 4)

def getSpots(band, spotband):
        xml = requests.get(
            url="http://dxlite.g7vjr.org/?xml=1&band=" + spotband + "&dxcc=001&limit=5")
        spots = xmltodict.parse(xml.text)
        sleep(5)
        print("Last 5 Spots for " + band + "\n")
        for spots in spots["spots"]["spot"]:
            date_string = spots["time"]
            utc = pytz.utc
            est = pytz.timezone("US/Eastern")
            utc_datetime = utc.localize(
                datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S"))
            lcd.clear()
            lcd.display_string(progName, 1)
            lcd.display_string("Last 5 Spots for " + band, 2)
            lcd.display_string(spots["spotter"] + " -> " + spots["dx"], 3)
            lcd.display_string(spots["frequency"].split(".")[0] + " - " + utc_datetime.astimezone(
                est).strftime("%d %b ") + utc_datetime.astimezone(est).strftime("%H:%M"), 4)
            print(spots["spotter"] + " -> " + spots["dx"])
            print(spots["frequency"].split(".")[0] + " - " + utc_datetime.astimezone(
                est).strftime("%d %b ") + utc_datetime.astimezone(est).strftime("%H:%M"))
            sleep(3)

def relayPress(self=None, relayNum=None):
    band = relayPins[relayNum]["band"]
    spotband = relayPins[relayNum]["spotband"]
    if GPIO.input(relayNum) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        GPIO.output(relayNum, GPIO.LOW)
        tuning(band)
        tuned(band)
    elif GPIO.input(relayNum) == False:
        alreadyTuned(band)
        getSpots(band, spotband)
        tuned(band)
    return

def queryPins(self=None):
    for k,v in relayPins.items():
        if GPIO.input(k) == False:
            print("\nCurrent band: " + v["band"] + "\n")
            lcd.clear()
            lcd.display_string(progName, 1)
            lcd.display_string(k + " selected.", 2)
            lcd.display_string(readyMsg, 4)
        else:
            continue

def destroy():
    lcd.clear()
    lcd.display_string(progName, 1)
    lcd.display_string("Goodbye.", 3)
    print ("\nCleaning up...\n")
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.cleanup()
    sleep(.5)
    print ("\nGoodbye.\n")
    lcd.clear()
    lcd.switch_backlight(0)
    exit()

if __name__ == '__main__':
    __init__()
    while True:
        if args.cli:
            print("1. Select 80 Meters Low")
            print("2. Select 80 Meters High")
            print("3. Select 40 Meters Low")
            print("4. Select 40 Meters High")
            print("5. Select 20 Meters Low")
            print("6. Select 20 Meters High")
            print("7. Select 15 Meters")
            print("8. Select 10 Meters")
            print("9. Query band")
            print("0. Quit")
            try:
                selection=int(input("Select an option: "))
                if selection==1:
                    relayPress(relayNum=11)
                    continue
                elif selection==2:
                    relayPress(relayNum=12)
                    continue
                elif selection==3:
                    relayPress(relayNum=13)
                    continue
                elif selection==4:
                    relayPress(relayNum=14)
                    continue
                elif selection==5:
                    relayPress(relayNum=15)
                    continue
                elif selection==6:
                    relayPress(relayNum=16)
                    continue
                elif selection==7:
                    relayPress(relayNum=17)
                    continue
                elif selection==8:
                    relayPress(relayNum=18)
                    continue
                elif selection==9:
                    queryPins()
                    continue
                elif selection==0:
                    destroy()
                else:
                    print("\nInvalid choice. Enter 1-9.\n")
            except ValueError as e:
                print("\nInvalid choice. Enter 1-9.\n")
            except TypeError as e:
                print("\nInvalid choice. Enter 1-9.\n")
            except NameError as e:
                print("\nInvalid choice. Enter 1-9.\n")
            except KeyboardInterrupt:
                destroy()

        else:
            try:
                sleep(0.1)
            except ValueError as e:
                sleep(0.1)
            except TypeError as e:
                sleep(0.1)
            except NameError as e:
                sleep(0.1)
            except KeyboardInterrupt:
                destroy()
