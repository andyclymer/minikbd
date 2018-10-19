from digitalio import DigitalInOut, Direction, Pull

class Encoder:
	
	"""
	CircuitPython Rotary Encoder (without interrupts)
	2017_10_16 Andy Clymer
	"""
	
	def __init__(self, pin1, pin2, upCallback=None, downCallback=None):
		# Init pins
		self.d1 = DigitalInOut(pin1)
		self.d1.direction = Direction.INPUT
		self.d1.pull = Pull.UP
		self.d2 = DigitalInOut(pin2)
		self.d2.direction = Direction.INPUT
		self.d2.pull = Pull.UP
		# Callbacks
		self.upCallback = upCallback
		self.downCallback = downCallback
		# Values for comparison
		self.prev1 = 0
		self.prev2 = 0
		self.new1 = 0
		self.new2 = 0
		self.lastFewDirs = [0, 0, 0, 0]
		# Encoder truth table
		self.encTable = {
			(1, 1): {(1, 0):1, (1, 1):0, (0, 1):-1, (0, 0):2},
			(1, 0): {(0, 0):1, (1, 0):0, (1, 1):-1, (0, 1):2},
			(0, 0): {(0, 1):1, (0, 0):0, (1, 0):-1, (1, 1):2},
			(0, 1): {(1, 1):1, (0, 1):0, (0, 0):-1, (1, 0):2}}
	
	def update(self):
		self.new1 = self.d1.value
		self.new2 = self.d2.value
		# Pin values changed:
		if not (self.prev1, self.prev2) == (self.new1, self.new2):
			# Determine out the dirction
			newDir = self.encTable[(self.prev1, self.prev2)][(self.new1, self.new2)]
			self.prev1 = self.new1
			self.prev2 = self.new2
			# Hold on to this new direction with the last three
			self.lastFewDirs = self.lastFewDirs[1:] + [newDir]
			# A good reading has four values of the same direction.
			# If the list adds up as expected, return the direction and rest the list
			s = sum(self.lastFewDirs)
			if s == 4:
				self.lastFewDirs = [0, 0, 0, 0]
				if self.upCallback: self.upCallback()
			elif s == -4:
				self.lastFewDirs = [0, 0, 0, 0]
				if self.downCallback: self.downCallback()
		return None