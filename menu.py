#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
from rpi_displays.sainsmart.displays import LCD2004

lcd=LCD2004()

relay1=11
relay2=12
relay3=13
relay4=14
relay5=15
relay6=16
relay7=17
relay8=18
button1=21
button2=20
button3=26
button4=19
button5=6
button6=5

relayPins={"relay1": 11, "relay2": 12, "relay3": 13, "relay4": 14, "relay5": 15, "relay6": 16, "relay7": 17, "relay8": 18}
allRelays = list(relayPins.values())

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(allRelays, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def __init__():
    lcd.clear()
    lcd.display_string("CMC BH-30 Controller", 1)
    lcd.display_string("Ready...", 3)
    GPIO.add_event_detect(button1, GPIO.FALLING, callback=relayOne, bouncetime=1500)
    GPIO.add_event_detect(button2, GPIO.FALLING, callback=relayTwo, bouncetime=1500)
    GPIO.add_event_detect(button3, GPIO.FALLING, callback=relayThree, bouncetime=1500)
    GPIO.add_event_detect(button4, GPIO.FALLING, callback=relayFour, bouncetime=1500)
    GPIO.add_event_detect(button5, GPIO.FALLING, callback=relayFive, bouncetime=1500)
    GPIO.add_event_detect(button6, GPIO.FALLING, callback=relaySix, bouncetime=1500)

def relayOne():
    if GPIO.input(relay1) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(1)
        GPIO.output(relay1, GPIO.LOW)
        print ("\nRelay 1 is Selected.\n")
    elif GPIO.input(relay1) == False:
        print("\nRelay 1 is already selected!\n")
    return

def relayTwo():
    if GPIO.input(relay2) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(1)
        GPIO.output(relay2, GPIO.LOW)
        print ("\nRelay 2 Selected.\n")
    elif GPIO.input(relay2) == False:
        print("\nRelay 2 is already selected!\n")
    return

def relayThree():
    if GPIO.input(relay3) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(1)
        GPIO.output(relay3, GPIO.LOW)
        print ("\nRelay 3 Selected.\n")
    elif GPIO.input(relay3) == False:
        print("\nRelay 3 is already selected!\n")

def relayFour():
    if GPIO.input(relay4):
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(1)
        GPIO.output(relay4, GPIO.LOW)
        print ("\nRelay 4 Selected.\n")
    elif GPIO.input(relay4) == False:
        print("\nRelay 4 is already selected!\n")

def relayFive():
    if GPIO.input(relay5) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(1)
        GPIO.output(relay5, GPIO.LOW)
        print ("\nRelay 5 Selected.\n")
    elif GPIO.input(relay5) == False:
        print("\nRelay 5 is already selected!\n")

def relaySix():
    if GPIO.input(relay6) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(1)
        GPIO.output(relay6, GPIO.LOW)
        print ("\nRelay 6 Selected.\n")
    elif GPIO.input(relay6) == False:
        print("\nRelay 6 is already selected!\n")
    return

def relaySeven():
    if GPIO.input(relay7) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(1)
        GPIO.output(relay7, GPIO.LOW)
        print ("\nRelay 7 Selected.\n")
    elif GPIO.input(relay7) == False:
        print("\nRelay 7 is already selected!\n")

def relayEight():
    if GPIO.input(relay8) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(1)
        GPIO.output(relay8, GPIO.LOW)
        print ("\nRelay 8 Selected.\n")
    elif GPIO.input(relay8) == False:
        print("\nRelay 8 is already selected!\n")

def queryPins():

    for k,v in relayPins:
        if gpio.input(relayPins[k]) == False:
            print("False")
        else:
            return

#    for any in allRelays:
#        if any == False:
#            print("dickbutt")
#        else:
#            return

#    if GPIO.input(relay1):
#        print("\nRelay 1 is not active.\n")
#    else:
#        print("\nRelay 1 is active.\n")
#
#    if GPIO.input(relay2):
#        print("\nRelay 2 is not active.\n")
#    else:
#        print("\nRelay 2 is active.\n")
#
#    if GPIO.input(relay3):
#        print("\nRelay 3 is not active.\n")
#    else:
#        print("\nRelay 3 is active.\n")
#
#    if GPIO.input(relay4):
#        print("\nRelay 4 is not active.\n")
#    else:
#        print("\nRelay 4 is active.\n")
#
#    if GPIO.input(relay5):
#        print("\nRelay 5 is not active.\n")
#    else:
#        print("\nRelay 5 is active.\n")
#
#    if GPIO.input(relay6):
#        print("\nRelay 6 is not active.\n")
#    else:
#        print("\nRelay 6 is active.\n")
#
#    if GPIO.input(relay7):
#        print("\nRelay 7 is not active.\n")
#    else:
#        print("\nRelay 7 is active.\n")
#
#    if GPIO.input(relay8):
#        print("\nRelay 8 is not active.\n")
#    else:
#        print("\nRelay 8 is active.\n")

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
        print("1. Select relay 1")
        print("2. Select relay 2")
        print("3. Select relay 3")
        print("4. Select relay 4")
        print("5. Select relay 5")
        print("6. Select relay 6")
        print("7. Select relay 7")
        print("8. Select relay 8")
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
            print(e)
            print("\nInvalid choice. Enter 1-9.\n")
        except KeyboardInterrupt:
            destroy()
