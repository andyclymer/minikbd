import board
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import adafruit_dotstar as dotstar
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
from encoder import Encoder
import time
import random

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl()
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.5)

modeColors = [(0, 255, 128), (255, 0, 0)]
mode = 0
dot[0] = modeColors[0]

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
	global mode
	if mode == 0:
		cc.send(ConsumerControlCode.SCAN_NEXT_TRACK)
	elif mode == 1:
		kbd.press(Keycode.Z)
	kbd.release_all()

def enc1Down():
	global mode
	if mode == 0:
		cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
	elif mode == 1:
		kbd.press(Keycode.X)
	kbd.release_all()

def enc2Up():
	global mode
	if mode == 0:
		if not fastTurn():
			kbd.press(Keycode.ALT)
			kbd.press(Keycode.SHIFT)
		cc.send(ConsumerControlCode.VOLUME_INCREMENT)
	elif mode == 1:
		kbd.press(Keycode.RIGHT_BRACKET)
	kbd.release_all()

def enc2Down():
	global mode
	if mode == 0:
		if not fastTurn():
			kbd.press(Keycode.ALT)
			kbd.press(Keycode.SHIFT)
		cc.send(ConsumerControlCode.VOLUME_DECREMENT)
	elif mode == 1:
		kbd.press(Keycode.LEFT_BRACKET)
	kbd.release_all()

def button1():
	global mode
	if not fastTurn():
		mode += 1
		if mode >= len(modeColors):
			mode = 0
		dot[0] = modeColors[mode]

def button2():
	global mode
	if mode == 0:
		if not fastTurn():
			cc.send(ConsumerControlCode.PLAY_PAUSE)
	if mode == 1:
			kbd.press(Keycode.GUI)
			kbd.press(Keycode.ZERO)
	kbd.release_all()


e1 = Encoder(board.D4, board.D3, upCallback=enc1Up, downCallback=enc1Down)
e2 = Encoder(board.D1, board.D0, upCallback=enc2Up, downCallback=enc2Down)

buttonPin = AnalogIn(board.D2)


while True:
	
	e1.update()
	e2.update()

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

