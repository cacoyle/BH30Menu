#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
from rpi_displays.sainsmart.displays import LCD2004

lcd=LCD2004()

Relay1=11
Relay2=12
Relay3=13
Relay4=14
Relay5=15
Relay6=16
Relay7=17
Relay8=18
button1=21
button2=20
button3=26
button4=19
button5=6
button6=5
button7=25

relayPins={"Relay1": 11, "Relay2": 12, "Relay3": 13, "Relay4": 14, "Relay5": 15, "Relay6": 16, "Relay7": 17, "Relay8": 18}
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
GPIO.setup(button7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def __init__():
    lcd.clear()
    lcd.display_string("CMC BH-30 Controller", 1)
    lcd.display_string("Ready...      VA3DXV", 4)
    GPIO.add_event_detect(button1, GPIO.FALLING, callback=relayOne, bouncetime=5000)
    GPIO.add_event_detect(button2, GPIO.FALLING, callback=relayTwo, bouncetime=5000)
    GPIO.add_event_detect(button3, GPIO.FALLING, callback=relayThree, bouncetime=5000)
    GPIO.add_event_detect(button4, GPIO.FALLING, callback=relayFour, bouncetime=5000)
    GPIO.add_event_detect(button5, GPIO.FALLING, callback=relayFive, bouncetime=5000)
    GPIO.add_event_detect(button6, GPIO.FALLING, callback=relaySix, bouncetime=5000)
    GPIO.add_event_detect(button7, GPIO.FALLING, callback=relaySeven, bouncetime=5000)

def relayOne(self=None):
    sleep(.5)
    if GPIO.input(Relay1) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(.5)
        GPIO.output(Relay1, GPIO.LOW)
        print ("\nRelay 1 Selected.\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay1 selected.", 2)
        sleep(5)
        lcd.display_string("Ready...      VA3DXV", 4)
    elif GPIO.input(Relay1) == False:
        print("\nRelay 1 is already selected!\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Already on Relay1!", 3)
        sleep(1)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay1 selected.", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    return

def relayTwo(self=None):
    sleep(.5)
    if GPIO.input(Relay2) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(.5)
        GPIO.output(Relay2, GPIO.LOW)
        print ("\nRelay 2 Selected.\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay2 selected.", 2)
        sleep(5)
        lcd.display_string("Ready...      VA3DXV", 4)
    elif GPIO.input(Relay2) == False:
        print("\nRelay 2 is already selected!\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Already on Relay2!", 3)
        sleep(1)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay2 selected.", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    return

def relayThree(self=None):
    sleep(.5)
    if GPIO.input(Relay3) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(.5)
        GPIO.output(Relay3, GPIO.LOW)
        print ("\nRelay 3 Selected.\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay3 selected.", 2)
        sleep(5)
        lcd.display_string("Ready...      VA3DXV", 4)
    elif GPIO.input(Relay3) == False:
        print("\nRelay 3 is already selected!\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Already on Relay3!", 3)
        sleep(1)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay3 selected.", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    return

def relayFour(self=None):
    sleep(.5)
    if GPIO.input(Relay4):
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(.5)
        GPIO.output(Relay4, GPIO.LOW)
        print ("\nRelay 4 Selected.\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay4 selected.", 2)
        sleep(5)
        lcd.display_string("Ready...      VA3DXV", 4)
    elif GPIO.input(Relay4) == False:
        print("\nRelay 4 is already selected!\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Already on Relay4!", 3)
        sleep(1)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay4 selected.", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    return

def relayFive(self=None):
    sleep(.5)
    if GPIO.input(Relay5) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(.5)
        GPIO.output(Relay5, GPIO.LOW)
        print ("\nRelay 5 Selected.\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay5 selected.", 2)
        sleep(5)
        lcd.display_string("Ready...      VA3DXV", 4)
    elif GPIO.input(Relay5) == False:
        print("\nRelay 5 is already selected!\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Already on Relay5!", 3)
        sleep(1)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay5 selected.", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    return

def relaySix(self=None):
    sleep(.5)
    if GPIO.input(Relay6) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(.5)
        GPIO.output(Relay6, GPIO.LOW)
        print ("\nRelay 6 Selected.\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay6 selected.", 2)
        sleep(5)
        lcd.display_string("Ready...      VA3DXV", 4)
    elif GPIO.input(Relay6) == False:
        print("\nRelay 6 is already selected!\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Already on Relay6!", 3)
        sleep(1)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay6 selected.", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    return

def relaySeven(self=None):
    sleep(.5)
    if GPIO.input(Relay7) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(.5)
        GPIO.output(Relay7, GPIO.LOW)
        print ("\nRelay 7 Selected.\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay7 selected.", 2)
        sleep(5)
        lcd.display_string("Ready...      VA3DXV", 4)
    elif GPIO.input(Relay7) == False:
        print("\nRelay 7 is already selected!\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Already on Relay7!", 3)
        sleep(1)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay7 selected.", 2)
        lcd.display_string("Ready...      VA3DXV", 4)
    return

def relayEight(self=None):
    sleep(.5)
    if GPIO.input(Relay8) == True:
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(.5)
        GPIO.output(Relay8, GPIO.LOW)
        print ("\nRelay 8 Selected.\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay8 selected.", 2)
        sleep(5)
        lcd.display_string("Ready...      VA3DXV", 4)
    elif GPIO.input(Relay8) == False:
        print("\nRelay 8 is already selected!\n")
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Already on Relay8!", 3)
        sleep(1)
        lcd.clear()
        lcd.display_string("CMC BH-30 Controller", 1)
        lcd.display_string("Relay8 selected.", 2)
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
            print("\nInvalid choice. Enter 1-9.\n")
        except TypeError as e:
            print("\nInvalid choice. Enter 1-9.\n")
        except KeyboardInterrupt:
            destroy()
