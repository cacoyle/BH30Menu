#!/usr/bin/python3
import RPi.GPIO as GPIO
from bottle import route, run, template, request
from time import sleep

GPIO.setmode(GPIO.BCM)

Relay1=11
Relay2=12
Relay3=13
Relay4=14
Relay5=15
Relay6=16
Relay7=17
Relay8=18

relayPins={"Relay1": 11, "Relay2": 12, "Relay3": 13, "Relay4": 14, "Relay5": 15, "Relay6": 16, "Relay7": 17, "Relay8": 18}
allRelays = list(relayPins.values())

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(allRelays, GPIO.OUT, initial=GPIO.HIGH)

@route("/")
def index():
    return template("index.tpl")

@route("/80L")
@route("/80L/<name>")
def RelayOne(name="80L"):
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.output(Relay1, GPIO.LOW)
    return template("band.tpl", name=name)

@route("/80H")
@route("/80H/<name>")
def RelayTwo(name="80H"):
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.output(Relay2, GPIO.LOW)
    return template("band.tpl", name=name)

@route("/40L")
@route("/40L/<name>")
def RelayThree(name="40L"):
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.output(Relay3, GPIO.LOW)
    return template("band.tpl", name=name)

@route("/40H")
@route("/40H/<name>")
def RelayFour(name="40H"):
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.output(Relay4, GPIO.LOW)
    return template("band.tpl", name=name)

@route("/20L")
@route("/20L/<name>")
def RelayFive(name="20L"):
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.output(Relay5, GPIO.LOW)
    return template("band.tpl", name=name)

@route("/20H")
@route("/20H/<name>")
def RelaySix(name="20H"):
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.output(Relay6, GPIO.LOW)
    return template("band.tpl", name=name)

@route("/15")
@route("/15/<name>")
def RelaySeven(name="15"):
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.output(Relay7, GPIO.LOW)
    return template("band.tpl", name=name)

@route("/10")
@route("/10/<name>")
def RelayEight(name="10"):
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.output(Relay8, GPIO.LOW)
    return template("band.tpl", name=name)

def destroy():
    print ("\nCleaning up...\n")
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.cleanup()
    print ("\nGoodbye.\n")
    exit()

if __name__ == "__main__":
    try:
        run(host="0.0.0.0", port=80)
    except ValueError as e:
        print(e)
        destroy()
    except TypeError as e:
        print(e)
        destroy()
    except KeyboardInterrupt:
        print(e)
        destroy()
    finally:
        destroy()
