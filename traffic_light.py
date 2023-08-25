from gpiozero import LED, Button
from signal import pause
from time import sleep

red = LED(14)
yellow = LED(15)
green = LED(18)

#button = Button(2)
while True:
	red.on()
	sleep(4)
	red.off()
	yellow.on()
	sleep(2)
	yellow.off()
	green.on()
	sleep(4)
	green.off()
	yellow.on()
	sleep(2)
	yellow.off()
pause()
