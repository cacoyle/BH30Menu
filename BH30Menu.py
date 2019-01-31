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
import time
import datetime
import pytz
import requests
import argparse
import xmltodict
import socket
from time import sleep
from rpi_displays.sainsmart.displays import LCD2004

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

relayPins={"Relay1": 11, "Relay2": 12, "Relay3": 13, "Relay4": 14, "Relay5": 15, "Relay6": 16, "Relay7": 17, "Relay8": 18}
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
    lcd.display_string("CMC BH-30 Controller", 1)
    lcd.display_string("Ready...      VA3DXV", 4)
    GPIO.add_event_detect(Button1, GPIO.FALLING, callback=relayOne, bouncetime=500)
    GPIO.add_event_detect(Button2, GPIO.FALLING, callback=relayTwo, bouncetime=500)
    GPIO.add_event_detect(Button3, GPIO.FALLING, callback=relayThree, bouncetime=500)
    GPIO.add_event_detect(Button4, GPIO.FALLING, callback=relayFour, bouncetime=500)
    GPIO.add_event_detect(Button5, GPIO.FALLING, callback=relayFive, bouncetime=500)
    GPIO.add_event_detect(Button6, GPIO.FALLING, callback=relaySix, bouncetime=500)
    GPIO.add_event_detect(Button7, GPIO.FALLING, callback=relaySeven, bouncetime=500)
    GPIO.add_event_detect(Button8, GPIO.FALLING, callback=relayEight, bouncetime=500)

def relayOne(self=None):
    sleep(.5)
    if GPIO.input(Relay1) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(.5)
        GPIO.output(Relay1, GPIO.LOW)
        print ("\n80M Low Activated.\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Switching to 80 Low", 2)
        lcd.display_string("Wait...", 4)
        sleep(5)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Tuned to 80M Low", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    elif GPIO.input(Relay1) == False:
        print("\n80M Low is already selected!\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Already on 80M Low!", 3)
        lcd.display_string("Getting DX spots...", 4)
        xml_80L = requests.get(
            url="http://dxlite.g7vjr.org/?xml=1&band=80&dxcc=001&limit=5")
        spots_80L = xmltodict.parse(xml_80L.text)
        time.sleep(3)
        for spots in spots_80L["spots"]["spot"]:
            date_string = spots["time"]
            utc = pytz.utc
            est = pytz.timezone("US/Eastern")
            utc_datetime = utc.localize(
                datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S"))
            lcd.clear()
            lcd.display_string("CMC BH-30 Controller", 1)
            lcd.display_string("Last 5 Spots for 80M", 2)
            lcd.display_string(spots["spotter"] + "->" + spots["dx"], 3)
            lcd.display_string(spots["frequency"].split(".")[0] + " - " + utc_datetime.astimezone(
                est).strftime("%d %b ") + utc_datetime.astimezone(est).strftime("%H:%M"), 4)
            time.sleep(3)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Tuned to 80M Low", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    return

def relayTwo(self=None):
    sleep(.5)
    if GPIO.input(Relay2) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(.5)
        GPIO.output(Relay2, GPIO.LOW)
        print ("\n80M High Activated.\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Switching to 80 High", 2)
        lcd.display_string("Wait...", 4)
        sleep(5)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Tuned to 80M High", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    elif GPIO.input(Relay2) == False:
        print("\n80M High is already selected!\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Already on 80M High!", 3)
        lcd.display_string("Getting DX spots...", 4)
        xml_80H = requests.get(
            url="http://dxlite.g7vjr.org/?xml=1&band=80&dxcc=001&limit=5")
        spots_80H = xmltodict.parse(xml_80H.text)
        time.sleep(3)
        for spots in spots_80H["spots"]["spot"]:
            date_string = spots["time"]
            utc = pytz.utc
            est = pytz.timezone("US/Eastern")
            utc_datetime = utc.localize(
                datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S"))
            lcd.clear()
            lcd.display_string("CMC BH-30 Controller", 1)
            lcd.display_string("Last 5 Spots for 80M", 2)
            lcd.display_string(spots["spotter"] + "->" + spots["dx"], 3)
            lcd.display_string(spots["frequency"].split(".")[0] + " - " + utc_datetime.astimezone(
                est).strftime("%d %b ") + utc_datetime.astimezone(est).strftime("%H:%M"), 4)
            time.sleep(3)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Tuned to 80M High", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    return

def relayThree(self=None):
    sleep(.5)
    if GPIO.input(Relay3) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(.5)
        GPIO.output(Relay3, GPIO.LOW)
        print ("\n40M Low Activated.\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Switching to 40M Low", 2)
        lcd.display_string("Wait...", 4)
        sleep(5)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Tuned to 40M Low", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    elif GPIO.input(Relay3) == False:
        print("\n40M Low is already selected!\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Already on 40M Low!", 3)
        lcd.display_string("Getting DX spots...", 4)
        xml_40L = requests.get(
            url="http://dxlite.g7vjr.org/?xml=1&band=40&dxcc=001&limit=5")
        spots_40L = xmltodict.parse(xml_40L.text)
        time.sleep(3)
        for spots in spots_40L["spots"]["spot"]:
            date_string = spots["time"]
            utc = pytz.utc
            est = pytz.timezone("US/Eastern")
            utc_datetime = utc.localize(
                datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S"))
            lcd.clear()
            lcd.display_string("CMC BH-30 Controller", 1)
            lcd.display_string("Last 5 Spots for 40M", 2)
            lcd.display_string(spots["spotter"] + "->" + spots["dx"], 3)
            lcd.display_string(spots["frequency"].split(".")[0] + " - " + utc_datetime.astimezone(
                est).strftime("%d %b ") + utc_datetime.astimezone(est).strftime("%H:%M"), 4)
            time.sleep(3)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Tuned to 40M Low", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    return

def relayFour(self=None):
    sleep(.5)
    if GPIO.input(Relay4) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(.5)
        GPIO.output(Relay4, GPIO.LOW)
        print ("\n40M High Activated.\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Switching to 40 High", 2)
        lcd.display_string("Wait...", 4)
        sleep(5)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Tuned to 40M High", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    elif GPIO.input(Relay4) == False:
        print("\n40M High is already selected!\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Already on 40M High!", 3)
        lcd.display_string("Getting DX spots...", 4)
        xml_40H = requests.get(
            url="http://dxlite.g7vjr.org/?xml=1&band=40&dxcc=001&limit=5")
        spots_40H = xmltodict.parse(xml_40H.text)
        time.sleep(3)
        for spots in spots_40H["spots"]["spot"]:
            date_string = spots["time"]
            utc = pytz.utc
            est = pytz.timezone("US/Eastern")
            utc_datetime = utc.localize(
                datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S"))
            lcd.clear()
            lcd.display_string("CMC BH-30 Controller", 1)
            lcd.display_string("Last 5 Spots for 40M", 2)
            lcd.display_string(spots["spotter"] + "->" + spots["dx"], 3)
            lcd.display_string(spots["frequency"].split(".")[0] + " - " + utc_datetime.astimezone(
                est).strftime("%d %b ") + utc_datetime.astimezone(est).strftime("%H:%M"), 4)
            time.sleep(3)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Tuned to 40M High", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    return

def relayFive(self=None):
    sleep(.5)
    if GPIO.input(Relay5) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(.5)
        GPIO.output(Relay5, GPIO.LOW)
        print ("\n20M Low Activated.\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Switching to 20M Low", 2)
        lcd.display_string("Wait...", 4)
        sleep(5)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Tuned to 20M Low", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    elif GPIO.input(Relay5) == False:
        print("\n20M Low is already selected!\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Already on 20M Low!", 3)
        lcd.display_string("Getting DX spots...", 4)
        xml_20L = requests.get(
            url="http://dxlite.g7vjr.org/?xml=1&band=20&dxcc=001&limit=5")
        spots_20L = xmltodict.parse(xml_20L.text)
        time.sleep(3)
        for spots in spots_20L["spots"]["spot"]:
            date_string = spots["time"]
            utc = pytz.utc
            est = pytz.timezone("US/Eastern")
            utc_datetime = utc.localize(
                datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S"))
            lcd.clear()
            lcd.display_string("CMC BH-30 Controller", 1)
            lcd.display_string("Last 5 Spots for 20M", 2)
            lcd.display_string(spots["spotter"] + "->" + spots["dx"], 3)
            lcd.display_string(spots["frequency"].split(".")[0] + " - " + utc_datetime.astimezone(
                est).strftime("%d %b ") + utc_datetime.astimezone(est).strftime("%H:%M"), 4)
            time.sleep(3)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Tuned to 20M Low", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    return

def relaySix(self=None):
    sleep(.5)
    if GPIO.input(Relay6) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(.5)
        GPIO.output(Relay6, GPIO.LOW)
        print ("\n20M High Activated.\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Switching to 20 High", 2)
        lcd.display_string("Wait...", 4)
        sleep(5)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Tuned to 20M High", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    elif GPIO.input(Relay6) == False:
        print("\n20M High is already selected!\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Already on 20M High!", 3)
        lcd.display_string("Getting DX spots...", 4)
        xml_20H = requests.get(
            url="http://dxlite.g7vjr.org/?xml=1&band=20&dxcc=001&limit=5")
        spots_20H = xmltodict.parse(xml_20H.text)
        time.sleep(3)
        for spots in spots_20H["spots"]["spot"]:
            date_string = spots["time"]
            utc = pytz.utc
            est = pytz.timezone("US/Eastern")
            utc_datetime = utc.localize(
                datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S"))
            lcd.clear()
            lcd.display_string("CMC BH-30 Controller", 1)
            lcd.display_string("Last 5 Spots for 20M", 2)
            lcd.display_string(spots["spotter"] + "->" + spots["dx"], 3)
            lcd.display_string(spots["frequency"].split(".")[0] + " - " + utc_datetime.astimezone(
                est).strftime("%d %b ") + utc_datetime.astimezone(est).strftime("%H:%M"), 4)
            time.sleep(3)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Tuned to 20M High", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    return

def relaySeven(self=None):
    sleep(.5)
    if GPIO.input(Relay7) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(.5)
        GPIO.output(Relay7, GPIO.LOW)
        print ("\n15M Activated.\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Switching to 15M", 2)
        lcd.display_string("Wait...", 4)
        sleep(5)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Tuned to 15M", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    elif GPIO.input(Relay7) == False:
        print("\n15M is already selected!\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Already on 15M!", 3)
        lcd.display_string("Getting DX spots...", 4)
        xml_15 = requests.get(
            url="http://dxlite.g7vjr.org/?xml=1&band=15&dxcc=001&limit=5")
        spots_15 = xmltodict.parse(xml_15.text)
        time.sleep(3)
        for spots in spots_15["spots"]["spot"]:
            date_string = spots["time"]
            utc = pytz.utc
            est = pytz.timezone("US/Eastern")
            utc_datetime = utc.localize(
                datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S"))
            lcd.clear()
            lcd.display_string("CMC BH-30 Controller", 1)
            lcd.display_string("Last 5 Spots for 15M", 2)
            lcd.display_string(spots["spotter"] + "->" + spots["dx"], 3)
            lcd.display_string(spots["frequency"].split(".")[0] + " - " + utc_datetime.astimezone(
                est).strftime("%d %b ") + utc_datetime.astimezone(est).strftime("%H:%M"), 4)
            time.sleep(3)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Tuned to 15M", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    return

def relayEight(self=None):
    sleep(.5)
    if GPIO.input(Relay8) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(.5)
        GPIO.output(Relay8, GPIO.LOW)
        print ("\n10M Activated.\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Switching to 10M", 2)
        lcd.display_string("Wait...", 4)
        sleep(5)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Tuned to 10M", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    elif GPIO.input(Relay8) == False:
        print("\n10M is already selected!\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Already on 10M!", 3)
        lcd.display_string("Getting DX spots...", 4)
        xml_10 = requests.get(
            url="http://dxlite.g7vjr.org/?xml=1&band=10&dxcc=001&limit=5")
        spots_10 = xmltodict.parse(xml_10.text)
        time.sleep(3)
        for spots in spots_10["spots"]["spot"]:
            date_string = spots["time"]
            utc = pytz.utc
            est = pytz.timezone("US/Eastern")
            utc_datetime = utc.localize(
                datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S"))
            lcd.clear()
            lcd.display_string("CMC BH-30 Controller", 1)
            lcd.display_string("Last 5 Spots for 10M", 2)
            lcd.display_string(spots["spotter"] + "->" + spots["dx"], 3)
            lcd.display_string(spots["frequency"].split(".")[0] + " - " + utc_datetime.astimezone(
                est).strftime("%d %b ") + utc_datetime.astimezone(est).strftime("%H:%M"), 4)
            time.sleep(3)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Tuned to 10M", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    return

def queryPins(self=None):
    for k,v in relayPins.items():
        if GPIO.input(relayPins[k]) == False:
            print("\nCurrent relay: " + k + "\n")
            lcd.clear()
            lcd.display_string("CMC BH-30 Controller", 1)
            lcd.display_string(k + " selected.", 2)
            lcd.display_string("Ready...      VA3DXV", 4)
        else:
            continue

def destroy():
    lcd.clear()
    lcd.display_string("CMC BH-30 Controller", 1)
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
            print("9. Query relays")
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
            except KeyboardInterrupt:
                destroy()

        else:
            try:
                sleep(0.1)
            except ValueError as e:
                print("\nInvalid choice. Enter 1-9.\n")
            except TypeError as e:
                print("\nInvalid choice. Enter 1-9.\n")
            except KeyboardInterrupt:
                destroy()
