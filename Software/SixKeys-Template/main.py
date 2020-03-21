import board
from digitalio import DigitalInOut, Direction, Pull
import adafruit_dotstar as dotstar
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import usb_hid

from miniKbdButtons import MiniKbdButtons

dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)
dot[0] = (0, 0, 0)

kbd = Keyboard(usb_hid.devices)
kbdLayout = KeyboardLayoutUS(kbd)

# Customize these keycodes
# https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode
buttonIDtoKeycode = {
	1: Keycode.ONE,
	2: Keycode.TWO,
	3: Keycode.THREE,
	4: Keycode.FOUR,
	5: Keycode.FIVE,
	6: Keycode.SIX}


def buttonDownCallback(buttonID, othersDown):
	kbd.press(buttonIDtoKeycode[buttonID])
	dot[0] = (255, 0, 0) # Red LED
	print("Button _down_", buttonID, othersDown)

def buttonUpCallback(buttonID):
	kbd.release(buttonIDtoKeycode[buttonID])
	dot[0] = (0, 0, 0)
	print("Button ^UPUP^", buttonID)


ButtonMatrix = MiniKbdButtons(
	keyDownCallback=buttonDownCallback, 
	keyUpCallback=buttonUpCallback)

# Main Loop
while True:
	ButtonMatrix.update()