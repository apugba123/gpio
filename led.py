from gpiozero import LED
from time import sleep

led = LED(17)

def dash():
	led.on()
	sleep(1.5)
	led.off()
	sleep(1)


def dot():
    led.on()
    sleep(0.5)
    led.off()
    sleep(1)

dash()
dot()
dash()
dot()
dash()
dot()
    
