import board
from digitalio import DigitalInOut, Direction, Pull

class MiniKbdButtons:
	
	def __init__(self, keyDownCallback=None, keyUpCallback=None,):
		# Callbacks
		self.downCback = keyDownCallback
		self.upCback = keyUpCallback
		# Button state and map
		self.state = []
		self.pins = {}
		self.btnMap = [
			dict(row="D0", col="D2", id=1),
			dict(row="D1", col="D2", id=2),
			dict(row="D0", col="D4", id=3),
			dict(row="D1", col="D4", id=4),
			dict(row="D0", col="D3", id=5),
			dict(row="D1", col="D3", id=6)]
		self.initPins()
	
	def initPins(self):
		# Rows
		for pn in ["D0", "D1"]:
			p = DigitalInOut(getattr(board, pn))
			p.direction = Direction.OUTPUT
			self.pins[pn] = p
		# Columns
		for pn in ["D2", "D4", "D3"]:
			p = DigitalInOut(getattr(board, pn))
			p.direction = Direction.INPUT
			p.pull = Pull.DOWN
			self.pins[pn] = p
	
	def update(self):
		# Compare old and new state
		oldSt = self.state
		newSt = []
		newBtn = None
		for btn in self.btnMap:
			r = self.pins[btn["row"]]
			r.value = True
			if self.pins[btn["col"]].value:
				newSt += [btn["id"]]
				if not btn["id"] in oldSt:
					newBtn = btn["id"]
			r.value = False
		# Callbacks
		for oID in oldSt:
			if not oID in newSt:
				self.upCback(oID)
		if newBtn:
			self.downCback(newBtn, newSt)
		self.state = newSt