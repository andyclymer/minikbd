# MiniKbd Software — One Encoder and Two Keys

This is the basic starting point for code that works with the build option of one rotary encoder and two keyboard keys.

### How to use this sample code

Copy the `main.py`, `encoder.py` and `buttonMatrix.py` to the root level of your Trinket M0. The `main.py` code is run every time the Trinket reboots, and it imports code from the `encoder` and `buttonMatrix` libraries.

Before editing, I have some general advice for working with the MiniKBD one level back in the [Software](../) directory of this repo.

The `main.py` script contains the code that you'll edit to customize how the device works. Space is limited on the Trinket M0 so I'm providing a commented version of the code here to explain how it works (the comments would take up valuable space that you should be using for your code!)

```python
import board

# Import the Encoder and ButtonMatrix libraries that I've provided
from encoder import Encoder
from buttonMatrix import ButtonMatrix


# Encoder callbacks
# Each time the rotary encoder moves one notch "up" or one notch "down" these functions are called
# You'll edit these: replace the print statements with whatever you want the device to do when
# the rotary encdoer is rotated.

def rotatedUp():
	print("Up!")

def rotatedDown():
	print("Down!")


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
	print("Button %s down" % info["buttonID"])

def buttonUpCallback(info):
	print("Button %s down" % info["buttonID"])

def buttonHoldCallback(info):
	print("Button %s down" % info["buttonID"])


# In the "One Encoder and Two Keyboard Keys" build setup, key number 1 is connected to
# pins D0 and D2, and key number 2 is connected to pins D1 and D2. They're wired in a matrix: 
# a signal is applied to both keys through D2 and the MiniKBD can sense which key(s) are held 
# down by checkingthe inputs of D0 and D1.

buttonMap = [
	dict(sendPinName="D0", receivePinName="D2", buttonID=1),
	dict(sendPinName="D1", receivePinName="D2", buttonID=2)]

# Make a new ButtonMatrix object for these two keys. This takes care of checking the state of 
# the keys and it will call the button callback functions above when the state changes.

Matrix = ButtonMatrix(
	buttonMap, 
	keyDownCallback=buttonDownCallback,
	keyUpCallback=buttonUpCallback,
	keyHoldCallback=buttonHoldCallback,
	holdDelayTime=1,
	holdRepeatTime=0.1)

# Make a new object for the rotary encoder. This takes care of watching for changes in state
# to the encoder, it figures out if the encoder was rotating "up" or "down", and then calls
# the callback functions above.

Encoder = Encoder(board.D3, board.D4, upCallback=rotatedUp, downCallback=rotatedDown)

# The main loop for the script. Now that all of the callback functions are defined, and the
# objects are made, this script will continuously ask the Encoder and Matrix objects to update
# and check for a state change. When the state does change, the objects will call the callback
# functions at the top of this script.

while True:
	Encoder.update()
	Matrix.update()
  
  ```
