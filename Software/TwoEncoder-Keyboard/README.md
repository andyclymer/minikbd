# MiniKbd Software — Two Encoder Keyboard

This is the basic starting point for using two rotatry encoders as a keyboard.

As the rotary encoders turn, each click of the encoder triggers a keyboard command. This is really useful for the kinds of keystrokes that you might normally click repeatedly — the default here has one encoder typing "z" in one direction and "x" in the other which already map to the "Zoom In" and "Zoom Out" commands in the design application that I use. Instant zoom dial. Another idea could be to type the keyboard command for "Volume Up" with each click in one direction and "Volume Down" in another direction, I've provided this as a separate example in the same repo.

### How to use this sample code

Copy the `main.py` and `encoder.py` to the root level of your Trinket M0. The `main.py` code is run every time the Trinket reboots, and it imports code from the `encoder` library.

Before editing, I have some general advice for working with the MiniKBD one level back in the [Software](../) directory of this repo.

The `main.py` script contains the code that you'll edit to customize how the device works. Space is limited on the Trinket M0 so I'm providing a commented version of the code here to explain how it works (the comments would take up valuable space that you should be using for your code!)

```python
import board
import adafruit_dotstar as dotstar
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import time
import random

# Import the encoder library that I've provided
from encoder import Encoder

# Create an object for the RGB "Dotstar" LED on the Trinket
# and set the RGB value for Black, to get started.
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.1)
dot[0] = (0, 0, 0)

# Create a new Keyboard object. We'll send keyboard commands to this later.
kbd = Keyboard()

# Add a small 1/10 sec delay between button presses, otherwise clicking the encoder button might hit the callback several times
# This function will be checked before the button callback sends a keycode to the computer.
prevTurn = time.monotonic()
def fastClick():
	global prevTurn
	now = time.monotonic()
	diff = now - prevTurn
	prevTurn = now
	if diff < 0.1:
		return True
	return False

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
	print("enc-1-up")
	dot[0] = (255, random.randint(0, 255), 0)
	kbd.press(Keycode.Z)
	kbd.release_all()
	
def enc1Down():
	print("enc-1-down")
	dot[0] = (0, random.randint(0, 255), 255)
	kbd.press(Keycode.X)
	kbd.release_all()

# Then, the other encoder types the left bracket when rotated in one direction, and the right bracket
# when rotated the other direction. Again, in the application I use, these step up and down through
# the drawing layers. Between these two encoders I have a nice little interface!

def enc2Up():
	print("enc-2-up")
	dot[0] = (255, random.randint(0, 255), 0)
	kbd.press(Keycode.LEFT_BRACKET)
	kbd.release_all()

def enc2Down():
	print("enc-2-down")
	dot[0] = (0, random.randint(0, 255), 255)
	kbd.press(Keycode.RIGHT_BRACKET)
	kbd.release_all()

# The encoders also work like buttons when they're pressed down. The first encoeder (the one that was
# zooming in and out for me) will type Command-Zero which resets the zoom to 100%. The other
# encoder types Command-A when clicked down.
# Before returning the keycode, it calls the fastClick() function which will return True if 
# the button had been pressed down 1/10 sec previously.

def button1():
	if not fastClick():
		print("enc-1-button")
		# Press a combination of the command key and zero
		kbd.press(Keycode.GUI, Keycode.ZERO)
		kbd.release_all()
	
def button2():
	if not fastClick():
		print("enc-2-button")
		kbd.press(Keycode.GUI, Keycode.A)
		kbd.release_all()


# Make a new objects for the rotary encoders. These take care of watching for changes in state
# to the encoder, it figures out if the encoder was rotating "up" or "down", and then calls
# the callback functions above.

e1 = Encoder(board.D4, board.D3, upCallback=enc1Up, downCallback=enc1Down)
e2 = Encoder(board.D1, board.D0, upCallback=enc2Up, downCallback=enc2Down)

# The two encoders have buttons when they're clicked down, and they share an analog input pin.
# This will be explained a little bit more below.
buttonPin = AnalogIn(board.D2)


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
