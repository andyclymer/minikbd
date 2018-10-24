import board
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from digitalio import DigitalInOut, Direction, Pull
import time
import adafruit_dotstar as dotstar

from encoder import Encoder

dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.1)
dot[0] = (30, 0, 255)

kbd = Keyboard()
cc = ConsumerControl()


prevTime = time.monotonic()
def shortDelay(delayTime=0.1):
	global prevTime
	now = time.monotonic()
	diff = now - prevTime
	prevTime = now
	if diff < delayTime:
		return True
	return False


# Encoder callbacks

def rotatedUp():
	if not shortDelay():
		kbd.press(Keycode.ALT)
		kbd.press(Keycode.SHIFT)
	cc.send(ConsumerControlCode.VOLUME_INCREMENT)
	kbd.release_all()

def rotatedDown():
	if not shortDelay():
		kbd.press(Keycode.ALT)
		kbd.press(Keycode.SHIFT)
	cc.send(ConsumerControlCode.VOLUME_DECREMENT)
	kbd.release_all()

def button1Down():
	if not shortDelay(delayTime=0.01):
		cc.send(ConsumerControlCode.PLAY_PAUSE)

def button2Down():
	if not shortDelay(delayTime=0.01):
		cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)



button1Pin = DigitalInOut(board.D0)
button1Pin.direction = Direction.OUTPUT

button2Pin = DigitalInOut(board.D1)
button2Pin.direction = Direction.OUTPUT

buttonInPin = DigitalInOut(board.D2)
buttonInPin.direction = Direction.INPUT
buttonInPin.pull = Pull.DOWN

Encoder = Encoder(board.D4, board.D3, upCallback=rotatedUp, downCallback=rotatedDown)

while True:
	Encoder.update()
	# Btn 1
	button1Pin.value = True
	if buttonInPin.value:
		button1Down()
	button1Pin.value = False
	# Btn 2
	button2Pin.value = True
	if buttonInPin.value:
		button2Down()
	button2Pin.value = False
