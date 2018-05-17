import RPi.GPIO as GPIO
import dht11
import time
import datetime
import httplib, urllib

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=17)
validacion=True
while validacion:
	result = instance.read()
	if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %d C" % result.temperature)	
            print("Humidity: %d %%" % result.humidity)
            validacion=False