import board
from digitalio import DigitalInOut, Direction, Pull
import adafruit_dotstar as dotstar
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

from miniKbdButtons import MiniKbdButtons

dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)
dot[0] = (0, 0, 0)

kbd = Keyboard()
kbdLayout = KeyboardLayoutUS(kbd)

# Customize these keycodes
buttonIDtoKeycode = {
	1: Keycode.A,
	2: Keycode.RIGHT_ARROW,
	3: Keycode.UP_ARROW,
	4: Keycode.DOWN_ARROW,
	5: Keycode.SHIFT,
	6: Keycode.LEFT_ARROW}


def buttonDownCallback(buttonID, othersDown):
	kbd.press(buttonIDtoKeycode[buttonID])
	dot[0] = (255, 0, 0)
	print("Button _down_", info)

def buttonUpCallback(buttonID):
	kbd.release(buttonIDtoKeycode[buttonID])
	dot[0] = (0, 0, 0)
	print("Button ^UPUP^", info)


ButtonMatrix = MiniKbdButtons(
	keyDownCallback=buttonDownCallback, 
	keyUpCallback=buttonUpCallback)

# Main Loop
while True:
	ButtonMatrix.update()