# MiniKbd Software — Two Encoder Keyboard

This is the basic starting point for code that works with the build option of two rotary encoders..

As the rotary encoders turn, each click of the encoder triggers a keyboard command. The default here has one encoder typing "z" in one direction and "x" in the other, which map to the "Zoom In" and "Zoom Out" commands in the design application that I use, but feel free to customize as you wish!

### How to use this sample code

Copy the `main.py` and `encoder.py` to the root level of your Trinket M0. The `main.py` code is run every time the Trinket reboots, and it imports code from the `encoder` library.

Before editing, I have some general advice for working with the MiniKBD one level back in the [Software](../) directory of this repo.

The `main.py` script contains the code that you'll edit to customize how the device works. Space is limited on the Trinket M0 so I'm providing a commented version of the code here to explain how it works (the comments would take up valuable space that you should be using for your code!)

```python
import board
import adafruit_dotstar as dotstar
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import random

# Import the encoder library that I've provided
from encoder import Encoder

# Create an object for the RGB "Dotstar" LED on the Trinket
# and set the RGB value for Black, to get started.
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.1)
dot[0] = (0, 0, 0)

# Create a new Keyboard object. We'll send keyboard commands to this later.
kbd = Keyboard()


# Encoder callbacks

# Each time the rotary encoder moves one notch "up" or one notch "down" these functions are called
# You'll edit these: replace the print statements with whatever you want the device to do when
# the rotary encdoer is rotated.

# Customize the keycodes to change how the device functions.
# Each key has a number, and one keycode. The full list of keycodes can be found here:
# https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode

# The first encoder will type the letter "z" with each click when rotated in one direction,
# and the letter "x" when rotated in the other direction. In the design appliaction I use,
# these two keystrokes will zoom in and zoom out of the document. Nice!
# They also set the LED to be a random reddish color when rotated in one direction, and a
# random blueish color in the other direction.

def enc1Up():
	dot[0] = (255, random.randint(0, 255), 0)
	kbd.press(Keycode.Z)
	kbd.release_all()
	
def enc1Down():
	dot[0] = (0, random.randint(0, 255), 255)
	kbd.press(Keycode.X)
	kbd.release_all()

# Then, the other encoder types the left bracket when rotated in one direction, and the right bracket
# when rotated the other direction. Again, in the application I use, these step up and down through
# the drawing layers. Between these two encoders I have a nice little interface!

def enc2Up():
	dot[0] = (255, random.randint(0, 255), 0)
	kbd.press(Keycode.LEFT_BRACKET)
	kbd.release_all()

def enc2Down():
	dot[0] = (0, random.randint(0, 255), 255)
	kbd.press(Keycode.RIGHT_BRACKET)
	kbd.release_all()

# The encoders also work like buttons when they're pressed down. The first encoeder (the one that was
# zooming in and out for me) will type Command-Zero which resets the zoom to 100%. The other
# encoder types Command-A when clicked down.

def button1():
	# Press a combination of the command key and zero
	kbd.press(Keycode.GUI, Keycode.ZERO)
	kbd.release_all()
	
def button2():
	kbd.press(Keycode.GUI, Keycode.A)
	kbd.release_all()


# Make a new objects for the rotary encoders. These take care of watching for changes in state
# to the encoder, it figures out if the encoder was rotating "up" or "down", and then calls
# the callback functions above.

e1 = Encoder(board.D1, board.D3, upCallback=enc1Up, downCallback=enc1Down)
e2 = Encoder(board.D0, board.D4, upCallback=enc2Up, downCallback=enc2Down)

# The two encoders have buttons when they're clicked down, and they share an analog input pin.
# This will be explained a little bit more below.
buttonPin = AnalogIn(board.A1)


# The main loop for the script. Now that all of the callback functions are defined, and the
# objects are made, this script will continuously ask the Encoder objects to update and check
# for a state change. When the state does change, the objects will call the callback functions 
# at the top of this script.

while True:
	
  # Check both encoders for a change
	e1.update()
	e2.update()
	
	# The two encoder buttons share one analog input pin (because only one pin is left!)
	# The buttons pass through resistors of different values, so buy comparing the analog
	# voltage we're able to see which buttons are being held down.
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
    
	# Now that we know which buttons are held down, call their callback functions
	if b1:
		button1()
	if b2:
		button2()


```
