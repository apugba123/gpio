
from gpiozero import LED, Button
from signal import pause
from time import sleep
import urllib2

led = LED(17)
button = Button(2)

def ifttt():
	urllib2.urlopen("https://maker.ifttt.com/trigger/button_pressed/with/key/cfYd2M9wT2UtEv7SrDHhMo").read()
button.when_pressed = ifttt

def dash():
        led.on()
        sleep(1.5)
        led.off()
        sleep(1)

def dot():
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)

def R():
    dot()
    dash()
    dot()

def E():
    dot()

def B():
    dash()
    dot()
    dot()
    dot()
def say_my_name(): 
        dot()
	dot()
	dot()
	dash()
	dash()
	dot()
	dot()
	dot()

button.when_pressed =ifttt 
button.when_released = led.off



pause()
