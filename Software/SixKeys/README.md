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

# Import the buttonMatrix library that I've provided
from buttonMatrix import ButtonMatrix

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
    1: Keycode.A,
    2: Keycode.RIGHT_ARROW,
    3: Keycode.UP_ARROW,
    4: Keycode.DOWN_ARROW,
    5: Keycode.SHIFT,
    6: Keycode.LEFT_ARROW}


# Key callbacks
# These functions are called when a key is pressed down, 
# when a key is released, and when a key is held down for a length of time.
# You'll edit these: replace the print statements with whatever you want the device to do when
# the keys are pressed or released.
#   An info dictionary is passed along with it, with some helpful data:
#     'buttonID' = 1 or 2, the key number
#     'repeating' = True/False
#     'holdTime' = How long the key has been held down for
#     'othersDown' = A list of other buttonIDs that were already held down when this one was pressed

def buttonDownCallback(info):
    # When a key is pressed, find its keycode in the buttonIDtoKeycode dictionary,
    # and tell the keyboard object to press this keycode.
    kbd.press(buttonIDtoKeycode[info["buttonID"]])
    # Change the LED color, make it blue if the key is repeating, or red if the key hasn't repeated yet
    if info["repeating"]:
        dot[0] = (0, 0, 255)
    else: dot[0] = (255, 0, 0)
    print("Button _down_", info)
            
def buttonUpCallback(info):
    # When a key has been lifted, find its keycode again in the buttonIDtoKeycode dictionary
    # and tell the keyboard to release that key. Without doing this, the key would still be held down!
    kbd.release(buttonIDtoKeycode[info["buttonID"]])
    dot[0] = (0, 0, 0)
    print("Button ^UPUP^", info)
            
def buttonHoldCallback(info):
    # If the ButtonMatrix library sees that the key has been held down, this function is called
    dot[0] = (255, 0, 128)
    print("Button hold", info)

# The six keys are wired in a matrix of rows and columns. A singnal is applied to the "sendPin"
# for each row, and then each column is tested to see which keys were actually held down.
# No need to change this dictionary, it matches the way the keyswitches are hard wired on the MiniKBD.
buttonMap = [
    dict(sendPinName="D0", receivePinName="D2", buttonID=1),
    dict(sendPinName="D1", receivePinName="D2", buttonID=2),
    dict(sendPinName="D0", receivePinName="D4", buttonID=3),
    dict(sendPinName="D1", receivePinName="D4", buttonID=4),
    dict(sendPinName="D0", receivePinName="D3", buttonID=5),
    dict(sendPinName="D1", receivePinName="D3", buttonID=6)]

# Make a new ButtonMatrix object for these two keys. This takes care of checking the state of 
# the keys and it will call the button callback functions above when the state changes.

Matrix = ButtonMatrix(
            buttonMap, 
            keyDownCallback=buttonDownCallback,
            keyUpCallback=buttonUpCallback,
            keyHoldCallback=buttonHoldCallback,
            holdDelayTime=1,
            holdRepeatTime=0.1)

# The main loop for the script. Now that all of the callback functions are defined, and the
# objects are made, this script will continuously ask the Matrix object to update and check
# for a state change. When the state does change, the objects will call the callback functions 
# at the top of this script.

while True:
    Matrix.update()
```
