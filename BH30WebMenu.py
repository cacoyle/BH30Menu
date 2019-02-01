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

@route('/')

def index():
    return template('home.tpl')

@route('/80L')
def index():
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.output(Relay1, GPIO.LOW)
    return template('home.tpl')

@route('/80H')
def index():
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.output(Relay2, GPIO.LOW)
    return template('home.tpl')

@route('/40L')
def index():
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.output(Relay3, GPIO.LOW)
    return template('home.tpl')

@route('/40H')
def index():
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.output(Relay4, GPIO.LOW)
    return template('home.tpl')

@route('/20L')
def index():
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.output(Relay5, GPIO.LOW)
    return template('home.tpl')

@route('/20H')
def index():
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.output(Relay6, GPIO.LOW)
    return template('home.tpl')

@route('/15')
def index():
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.output(Relay7, GPIO.LOW)
    return template('home.tpl')

@route('/10')
def index():
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.output(Relay8, GPIO.LOW)
    return template('home.tpl')

def destroy():
    print ("\nCleaning up...\n")
    GPIO.output(allRelays, GPIO.HIGH)
    GPIO.cleanup()
    print ("\nGoodbye.\n")
    exit()

if __name__ == '__main__':
    try:
        run(host='192.168.100.250', port=80)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except KeyboardInterrupt:
        sleep(5)
        destroy()
