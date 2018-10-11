import board
import adafruit_dotstar as dotstar
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
from encoder import Encoder

import random

dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.1)
dot[0] = (0, 0, 0)

kbd = Keyboard()


# Encoder callbacks, rotating "up" and "down"

def enc1Up():
	dot[0] = (255, random.randint(0, 255), 0)
	kbd.press(Keycode.Z)
	kbd.release_all()
	
def enc1Down():
	dot[0] = (0, random.randint(0, 255), 255)
	kbd.press(Keycode.X)
	kbd.release_all()
	
def enc2Up():
	dot[0] = (255, random.randint(0, 255), 0)
	kbd.press(Keycode.LEFT_BRACKET)
	kbd.release_all()

def enc2Down():
	dot[0] = (0, random.randint(0, 255), 255)
	kbd.press(Keycode.RIGHT_BRACKET)
	kbd.release_all()
	
def button1():
	kbd.press(Keycode.GUI, Keycode.ZERO)
	kbd.release_all()
	
def button2():
	kbd.press(Keycode.GUI, Keycode.A)
	kbd.release_all()


e1 = Encoder(board.D1, board.D3, upCallback=enc1Up, downCallback=enc1Down)
e2 = Encoder(board.D0, board.D4, upCallback=enc2Up, downCallback=enc2Down)

buttonPin = AnalogIn(board.A1)


while True:
	
	e1.update()
	e2.update()
	
	# The encoder buttons combine to give an analog voltage
	# Determine which buttons are currently down
	v = buttonPin.value
	if 65535 > v > 54500:
		b1 = False
		b2 = False
	elif 54500 > v > 38500:
		b1 = True
		b2 = False
	elif 38500 > v > 29400:
		b1 = False
		b2 = True
	elif v < 29400:
		b1 = True
		b2 = True

	if b1:
		button1()
	if b2:
		button2()

