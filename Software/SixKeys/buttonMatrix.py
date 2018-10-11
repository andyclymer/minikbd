import board
from digitalio import DigitalInOut, Direction, Pull
import time

class Button(object):
    
    def __init__(self, parent):
        self.parent = parent
        self.sPin = None
        self.rPin = None
        self.downCback = None
        self.upCback = None
        self.holdCbk = None
        self.id = None
        self.state = False
        self.lastChangeTime = 0
        self.lastRepeatTIme = 0
        self.holding = False
    
    def info(self):
        holdTime = time.monotonic() - self.lastChangeTime
        othersDown = [b.id for b in self.parent._buttons if b.state if not b.id == self.id]
        return dict(buttonID=self.id, repeating=self.holding, holdTime=holdTime, othersDown=othersDown)
        
    def update(self):
        
        os = self.state # hold the old state
        self.sPin.value = True # Turn on the send pin
        ns = self.rPin.value # Check the new state
        if not os == ns:
            self.lastChangeTime = self.lastRepeatTime = time.monotonic()
            self.holding = False
            if ns == True:
                if self.downCback: self.downCback(info=self.info())
                if self.parent.downCback: self.parent.downCback(info=self.info())
            else:
                if self.upCback: self.upCback(info=i)
                if self.parent.upCback: self.parent.upCback(info=self.info())
        elif ns:
            if not self.holding:
                if time.monotonic() - self.lastChangeTime >= self.parent.holdDelayTime: 
                    if self.holdCbk: self.holdCbk(info=self.info())
                    if self.parent.holdCbk: self.parent.holdCbk(info=self.info())
                    self.holding = True
            else:
                if time.monotonic() - self.lastRepeatTime >= self.parent.holdRepeatTime: 
                    self.lastRepeatTime = time.monotonic()
                    if self.downCback: self.downCback(info=self.info())
                    if self.parent.downCback: self.parent.downCback(info=self.info())
        self.state = ns
        self.sPin.value = False
        
        

class ButtonMatrix:
    """
    Controller for a matrix of buttons.
    Each button is connected to a "send" and "receive" pin
    
        buttonMap = [
            dict(sPinName="D0", rPinName="D2", btnID=1),
            dict(sPinName="D0", rPinName="D4", btnID=2)]
        Matrix = ButtonMatrix(buttonMap)
    
    """
    def __init__(
            self, 
            buttonMap=[], 
            keyDownCallback=None, 
            keyUpCallback=None, 
            keyHoldCallback=None, 
            holdDelayTime=1, 
            holdRepeatTime=0.25):
        # Cbks
        self.downCback = keyDownCallback
        self.upCback = keyUpCallback
        self.holdCbk = keyHoldCallback
        # Buttons and pins
        self._buttons = [] # List of button objects
        self._pinMap = {} # Each pin name, mapped to a pin object, for easier button setup
        # Hold and repeat times
        self.holdDelayTime = holdDelayTime 
        self.holdRepeatTime = holdRepeatTime
        # Initialize
        self.initPins(buttonMap)
    
    def initPins(self, buttonMap):
        # Initialize pins and make Button objects
        for item in buttonMap:
            button = Button(self)
            button.id = item.get("buttonID", None)
            button.downCback = item.get("keyDownCallback", None)
            button.upCback = item.get("keyUpCallback", None)
            button.holdCbk = item.get("keyHoldCallback", None)
            if not item["sendPinName"] in self._pinMap:
                sPin = DigitalInOut(getattr(board, item["sendPinName"]))
                sPin.direction = Direction.OUTPUT
                self._pinMap[item["sendPinName"]] = sPin
            button.sPin = self._pinMap[item["sendPinName"]]
            if not item["receivePinName"] in self._pinMap:
                rPin = DigitalInOut(getattr(board, item["receivePinName"]))
                rPin.direction = Direction.INPUT
                rPin.pull = Pull.DOWN
                self._pinMap[item["receivePinName"]] = rPin
            button.rPin = self._pinMap[item["receivePinName"]]
            self._buttons.append(button)
    
    def update(self):
        # Check each button object
        for button in self._buttons:
            button.update()
          
          