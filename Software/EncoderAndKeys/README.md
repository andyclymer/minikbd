# MiniKbd Software — One Encoder and Two Keys

This is the basic starting point for code that works with the build option of one rotary encoder and two keyboard keys.

### How to use this sample code

Copy the `main.py`, `encoder.py` and `buttonMatrix.py` to the root level of your Trinket M0. The `main.py` code is run every time the Trinket reboots, and it imports code from the `encoder` and `buttonMatrix` libraries.

Before editing, I have some general advice for working with the MiniKBD one level back in the [Software](../) directory of this repo.

The `main.py` script contains the code that you'll edit to customize how the device works. Space is limited on the Trinket M0 so I'm providing a commented version of the code here to explain how it works (the comments would take up valuable space that you should be using for your code!)

```python
import board
# Import the Encoder and ButtonMatrix libraries
from encoder import Encoder
from buttonMatrix import ButtonMatrix


# Encoder callbacks

# Each time the rotary encoder moves one notch "up", this function is run.
def rotatedUp():
	print("Up!")
	
def rotatedDown():
	print("Down!")


# Key callbacks

def buttonDownCallback(info):
	print("Button %s down" % info["buttonID"])

def buttonUpCallback(info):
	print("Button %s down" % info["buttonID"])

def buttonHoldCallback(info):
	print("Button %s down" % info["buttonID"])


buttonMap = [
	dict(sendPinName="D0", receivePinName="D2", buttonID=1),
	dict(sendPinName="D1", receivePinName="D2", buttonID=2)]

Matrix = ButtonMatrix(
	buttonMap, 
	keyDownCallback=buttonDownCallback,
	keyUpCallback=buttonUpCallback,
	keyHoldCallback=buttonHoldCallback,
	holdDelayTime=1,
	holdRepeatTime=0.1)

Encoder = Encoder(board.D3, board.D4, upCallback=rotatedUp, downCallback=rotatedDown)

while True:
	Encoder.update()
	Matrix.update()
  
  ```
