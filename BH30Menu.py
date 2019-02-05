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

Relay1=11
Relay2=12
Relay3=13
Relay4=14
Relay5=15
Relay6=16
Relay7=17
Relay8=18
Button1=21
Button2=20
Button3=26
Button4=19
Button5=6
Button6=5
Button7=25
Button8=24

relayPins={"80M Low": 11, "80M High": 12, "40M Low": 13, "40M High": 14, "20M Low": 15, "20M High": 16, "15M": 17, "10M": 18}
allRelays = list(relayPins.values())

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(allRelays, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button8, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def __init__():
    lcd.clear()
    lcd.display_string(progName, 1)
    lcd.display_string(readyMsg, 4)
    GPIO.add_event_detect(Button1, GPIO.FALLING, callback=relayOne, bouncetime=500)
    GPIO.add_event_detect(Button2, GPIO.FALLING, callback=relayTwo, bouncetime=500)
    GPIO.add_event_detect(Button3, GPIO.FALLING, callback=relayThree, bouncetime=500)
    GPIO.add_event_detect(Button4, GPIO.FALLING, callback=relayFour, bouncetime=500)
    GPIO.add_event_detect(Button5, GPIO.FALLING, callback=relayFive, bouncetime=500)
    GPIO.add_event_detect(Button6, GPIO.FALLING, callback=relaySix, bouncetime=500)
    GPIO.add_event_detect(Button7, GPIO.FALLING, callback=relaySeven, bouncetime=500)
    GPIO.add_event_detect(Button8, GPIO.FALLING, callback=relayEight, bouncetime=500)

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

def relayOne(self=None, band="80M Low", spotband="80"):
    if GPIO.input(Relay1) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        GPIO.output(Relay1, GPIO.LOW)
        tuning(band)
        tuned(band)
    elif GPIO.input(Relay1) == False:
        alreadyTuned(band)
        getSpots(band, spotband)
        tuned(band)
    return

def relayTwo(self=None, band="80M High", spotband="80"):
    if GPIO.input(Relay2) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        GPIO.output(Relay2, GPIO.LOW)
        tuning(band)
        tuned(band)
    elif GPIO.input(Relay2) == False:
        alreadyTuned(band)
        getSpots(band, spotband)
        tuned(band)
    return

def relayThree(self=None, band="40M Low", spotband="40"):
    if GPIO.input(Relay3) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        GPIO.output(Relay3, GPIO.LOW)
        tuning(band)
        tuned(band)
    elif GPIO.input(Relay3) == False:
        alreadyTuned(band)
        getSpots(band, spotband)
        tuned(band)
    return

def relayFour(self=None, band="40M High", spotband="40"):
    if GPIO.input(Relay4) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        GPIO.output(Relay4, GPIO.LOW)
        tuning(band)
        tuned(band)
    elif GPIO.input(Relay4) == False:
        alreadyTuned(band)
        getSpots(band, spotband)
        tuned(band)
    return

def relayFive(self=None, band="20M Low", spotband="20"):
    if GPIO.input(Relay5) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        GPIO.output(Relay5, GPIO.LOW)
        tuning(band)
        tuned(band)
    elif GPIO.input(Relay5) == False:
        alreadyTuned(band)
        getSpots(band, spotband)
        tuned(band)
    return

def relaySix(self=None, band="20M High", spotband="20"):
    if GPIO.input(Relay6) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        GPIO.output(Relay6, GPIO.LOW)
        tuning(band)
        tuned(band)
    elif GPIO.input(Relay6) == False:
        alreadyTuned(band)
        getSpots(band, spotband)
        tuned(band)
    return

def relaySeven(self=None, band="15M", spotband="15"):
    if GPIO.input(Relay7) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        GPIO.output(Relay7, GPIO.LOW)
        tuning(band)
        tuned(band)
    elif GPIO.input(Relay7) == False:
        alreadyTuned(band)
        getSpots(band, spotband)
        tuned(band)
    return

def relayEight(self=None, band="10M", spotband="10"):
    if GPIO.input(Relay8) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        GPIO.output(Relay8, GPIO.LOW)
        tuning(band)
        tuned(band)
    elif GPIO.input(Relay8) == False:
        alreadyTuned(band)
        getSpots(band, spotband)
        tuned(band)
    return

def queryPins(self=None):
    for k,v in relayPins.items():
        if GPIO.input(relayPins[k]) == False:
            print("\nCurrent band: " + k + "\n")
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
                    relayOne()
                    continue
                elif selection==2:
                    relayTwo()
                    continue
                elif selection==3:
                    relayThree()
                    continue
                elif selection==4:
                    relayFour()
                    continue
                elif selection==5:
                    relayFive()
                    continue
                elif selection==6:
                    relaySix()
                    continue
                elif selection==7:
                    relaySeven()
                    continue
                elif selection==8:
                    relayEight()
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
