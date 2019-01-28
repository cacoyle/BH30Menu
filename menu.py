#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
import lcddriver
lcd = lcddriver.lcd()
lcd.lcd_clear()
lcd.lcd_display_string("CMC BH-30 Controller", 1)
lcd.lcd_display_string("Ready...", 3)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

allRelays=[11,12,13,14,15,16,17,18]
relay1=11
relay2=12
relay3=13
relay4=14
relay5=15
relay6=16
relay7=17
relay8=18

GPIO.setup(allRelays, GPIO.OUT, initial=GPIO.HIGH)

state1=GPIO.input(relay1)
state2=GPIO.input(relay2)
state3=GPIO.input(relay3)
state4=GPIO.input(relay4)
state5=GPIO.input(relay5)
state6=GPIO.input(relay6)
state7=GPIO.input(relay7)
state8=GPIO.input(relay8)

def main():
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
    while True:
        try:
            selection=int(input("Select an option: "))
            if selection==1:
                relayOne()
                break
            elif selection==2:
                relayTwo()
                break
            elif selection==3:
                relayThree()
                break
            elif selection==4:
                relayFour()
                break
            elif selection==5:
                relayFive()
                break
            elif selection==6:
                relaySix()
                break
            elif selection==7:
                relaySeven()
                break
            elif selection==8:
                relayEight()
                break
            elif selection==9:
                queryPins()
                break
            elif selection==0:
                destroy()
            else:
                print("\nInvalid choice. Enter 1-3.\n")
                main()
        except ValueError as e:
                print(e)
                print("\nInvalid choice. Enter 1-3.\n")

def relayOne():
    if GPIO.input(relay1):
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(1)
        GPIO.output(relay1, GPIO.LOW)
        print ("\nRelay 1 is Selected.\n")
    else:
        print("\nRelay 1 is already selected!\n")
    main()

def relayTwo():
    if GPIO.input(relay2):
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(1)
        GPIO.output(relay2, GPIO.LOW)
        print ("\nRelay 2 Selected.\n")
    else:
        print("\nRelay 2 is already selected!\n")
    main()

def relayThree():
    if GPIO.input(relay3):
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(1)
        GPIO.output(relay3, GPIO.LOW)
        print ("\nRelay 3 Selected.\n")
    else:
        print("\nRelay 3 is already selected!\n")
    main()

def relayFour():
    if GPIO.input(relay4):
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(1)
        GPIO.output(relay4, GPIO.LOW)
        print ("\nRelay 4 Selected.\n")
    else:
        print("\nRelay 4 is already selected!\n")
    main()

def relayFive():
    if GPIO.input(relay5):
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(1)
        GPIO.output(relay5, GPIO.LOW)
        print ("\nRelay 5 Selected.\n")
    else:
        print("\nRelay 5 is already selected!\n")
    main()

def relaySix():
    if GPIO.input(relay6):
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(1)
        GPIO.output(relay6, GPIO.LOW)
        print ("\nRelay 6 Selected.\n")
    else:
        print("\nRelay 6 is already selected!\n")
    main()

def relaySeven():
    if GPIO.input(relay7):
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(1)
        GPIO.output(relay7, GPIO.LOW)
        print ("\nRelay 7 Selected.\n")
    else:
        print("\nRelay 7 is already selected!\n")
    main()

def relayEight():
    if GPIO.input(relay8):
        GPIO.output(allRelays, GPIO.HIGH)
        sleep(1)
        GPIO.output(relay8, GPIO.LOW)
        print ("\nRelay 8 Selected.\n")
    else:
        print("\nRelay 8 is already selected!\n")
    main()

def queryPins():

    if GPIO.input(relay1):
        print("\nRelay 1 is not active.\n")
    else:
        print("\nRelay 1 is active.\n")

    if GPIO.input(relay2):
        print("\nRelay 2 is not active.\n")
    else:
        print("\nRelay 2 is active.\n")

    if GPIO.input(relay3):
        print("\nRelay 3 is not active.\n")
    else:
        print("\nRelay 3 is active.\n")

    if GPIO.input(relay4):
        print("\nRelay 4 is not active.\n")
    else:
        print("\nRelay 4 is active.\n")

    if GPIO.input(relay5):
        print("\nRelay 5 is not active.\n")
    else:
        print("\nRelay 5 is active.\n")

    if GPIO.input(relay6):
        print("\nRelay 6 is not active.\n")
    else:
        print("\nRelay 6 is active.\n")

    if GPIO.input(relay7):
        print("\nRelay 7 is not active.\n")
    else:
        print("\nRelay 7 is active.\n")

    if GPIO.input(relay8):
        print("\nRelay 8 is not active.\n")
    else:
        print("\nRelay 8 is active.\n")

    main()

def destroy():
    lcd.lcd_clear()
    lcd.lcd_display_string("CMC BH-30 Controller", 1)
    lcd.lcd_display_string("Goodbye.", 3)
    print ("\nCleaning up...\n")
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.cleanup()
    sleep(.5)
    print ("\nGoodbye.\n")
    lcd.lcd_clear()
    exit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        destroy()

