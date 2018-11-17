import board
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
from encoder import Encoder
import time
import random

kbd = Keyboard()
cc = ConsumerControl()


prevTurn = time.monotonic()
def fastTurn():
	global prevTurn
	now = time.monotonic()
	diff = now - prevTurn
	prevTurn = now
	if diff < 0.1:
		return True
	return False


def enc1Up():
	cc.send(ConsumerControlCode.SCAN_NEXT_TRACK)

def enc1Down():
	cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)

def enc2Up():
	if not fastTurn():
		kbd.press(Keycode.ALT)
		kbd.press(Keycode.SHIFT)
	cc.send(ConsumerControlCode.VOLUME_INCREMENT)
	kbd.release_all()

def enc2Down():
	if not fastTurn():
		kbd.press(Keycode.ALT)
		kbd.press(Keycode.SHIFT)
	cc.send(ConsumerControlCode.VOLUME_DECREMENT)
	kbd.release_all()

def button1():
	if not fastTurn():
		cc.send(ConsumerControlCode.PLAY_PAUSE)

def button2():
	if not fastTurn():
		cc.send(ConsumerControlCode.PLAY_PAUSE)


e1 = Encoder(board.D1, board.D3, upCallback=enc1Up, downCallback=enc1Down)
e2 = Encoder(board.D4, board.D0, upCallback=enc2Up, downCallback=enc2Down)

buttonPin = AnalogIn(board.D2)


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

