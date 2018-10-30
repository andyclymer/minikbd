# MiniKbd Software — Six Keyswitches

This is the simplest way to get started with the "Six Keyswitches" build, it provides an easy way to assign a single keystroke to each key. Other more complex examples are also available.

### How to use this sample code

Copy the `main.py` and `buttonMatrix.py` to the root level of your Trinket M0. The `main.py` code is run every time the Trinket reboots, and it imports code from the `buttonMatrix` library.

Before editing, I have some general advice for working with the MiniKBD one level back in the [Software](../) directory of this repo.

The basic principle is that you will want to edit the `buttonIDtoKeycode` dictionary in the `main.py` to customize the keyboard.

```python
buttonIDtoKeycode = {
    1: Keycode.SHIFT,
    2: Keycode.RIGHT_ARROW,
    3: Keycode.UP_ARROW,
    4: Keycode.DOWN_ARROW,
    5: Keycode.SHIFT,
    6: Keycode.LEFT_ARROW}
 ```
Each key is assigned a keycode in this dictionary. A full list of keycodes can be found in the [CircuitPython keycode docs](https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html). When looking directly at the keyboard, the keys are numbered in the following arrangement:
 
 ```
 ┏━┷┷━┯━━━┯━━━┯━━━┓
 ┃°  °│ 5 │ 3 │ 1 ┃
 ┃    ├───┼───┼───┨
 ┃°  °│ 6 │ 4 │ 2 ┃
 ┗━━━━┷━━━┷━━━┷━━━┛
 
```

The `main.py` script contains the code that you'll edit to customize how the device works. Space is limited on the Trinket M0 so I'm providing a commented version of the code here to explain how it works (the comments would take up valuable space that you should be using for your code!)

```python
import board
from digitalio import DigitalInOut, Direction, Pull
import adafruit_dotstar as dotstar
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Import the MiniKbdButtons library that I've provided
# All of the code that deals with reacting to key changes is kept in here
from miniKbdButtons import MiniKbdButtons

# Create an object for the RGB "Dotstar" LED on the Trinket
# and set the RGB value for Black, to get started.
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)
dot[0] = (0, 0, 0)

# Create a new Keyboard object. We'll send keyboard commands to this later.
kbd = Keyboard()
kbdLayout = KeyboardLayoutUS(kbd)

# Customize these keycodes to change how the device functions.
# Each key has a number, and one keycode. The full list of keycodes can be found here:
# https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode
buttonIDtoKeycode = {
	1: Keycode.ONE,
	2: Keycode.TWO,
	3: Keycode.THREE,
	4: Keycode.FOUR,
	5: Keycode.FIVE,
	6: Keycode.SIX}

# Key callbacks

# These functions are called when a key is pressed down and when a key is released.
# You'll edit these: replace the print statements with whatever you want the device to do when
# the keys are pressed or released.

# All of the buttons use the same callback functions, but the function receives the ID number of
# the key so you can program the callbacks to do different things depending on which key is held down.
# Another helpful thing is you'll also be given a list of othersDown which contains the button IDs
# for any other buttons that are also being held down.

# This simple example takes the buttonID and finds the keycode in the buttonIDtoKeycode dictionary
# (shown above) and then tells the keyboard object to press this keycode.

def buttonDownCallback(buttonID, othersDown):
    # When a key is pressed, find its keycode in the buttonIDtoKeycode dictionary,
    # and tell the keyboard object to press this keycode.
	kbd.press(buttonIDtoKeycode[buttonID])
	dot[0] = (255, 0, 0) # Turn the LED to be 100% Red and 0% Green and Blue
	print("Button _down_", buttonID, othersDown)

def buttonUpCallback(buttonID):
    # When a key has been lifted, find its keycode again in the buttonIDtoKeycode dictionary
    # and tell the keyboard to release that key. Without doing this, the key would still be held down!
	kbd.release(buttonIDtoKeycode[buttonID])
	dot[0] = (0, 0, 0)
	print("Button ^UPUP^", buttonID)

# Create a new MiniKbdButtons object, which we'll use in just a moment...
ButtonMatrix = MiniKbdButtons(
	keyDownCallback=buttonDownCallback, 
	keyUpCallback=buttonUpCallback)

# The main loop for the script. Now that all of the callback functions are defined, and the
# objects are made, this script will continuously ask the ButtonMatrix object to update and check
# for a state change. When the state does change, the objects will call the callback functions 
# at the top of this script.
while True:
	ButtonMatrix.update()
```
