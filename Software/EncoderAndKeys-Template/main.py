import board
from encoder import Encoder
from buttonMatrix import ButtonMatrix


# Encoder callbacks

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