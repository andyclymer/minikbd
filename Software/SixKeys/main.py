import board
from digitalio import DigitalInOut, Direction, Pull
import adafruit_dotstar as dotstar
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

from buttonMatrix import ButtonMatrix

dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)
dot[0] = (0, 0, 0)

kbd = Keyboard()
kbdLayout = KeyboardLayoutUS(kbd)

# Customize these keycodes
buttonIDtoKeycode = {
    1: Keycode.A,
    2: Keycode.RIGHT_ARROW,
    3: Keycode.UP_ARROW,
    4: Keycode.DOWN_ARROW,
    5: Keycode.SHIFT,
    6: Keycode.LEFT_ARROW}
    
    
def buttonDownCallback(info):
    kbd.press(buttonIDtoKeycode[info["buttonID"]])
    if info["repeating"]:
        dot[0] = (0, 0, 255)
    else: dot[0] = (255, 0, 0)
    print("Button _down_", info)
            
def buttonUpCallback(info):
    kbd.release(buttonIDtoKeycode[info["buttonID"]])
    dot[0] = (0, 0, 0)
    print("Button ^UPUP^", info)
            
def buttonHoldCallback(info):
    dot[0] = (255, 0, 128)
    print("Button hold", info)


buttonMap = [
    dict(sendPinName="D0", receivePinName="D2", buttonID=1),
    dict(sendPinName="D1", receivePinName="D2", buttonID=2),
    dict(sendPinName="D0", receivePinName="D4", buttonID=3),
    dict(sendPinName="D1", receivePinName="D4", buttonID=4),
    dict(sendPinName="D0", receivePinName="D3", buttonID=5),
    dict(sendPinName="D1", receivePinName="D3", buttonID=6)]

Matrix = ButtonMatrix(
            buttonMap, 
            keyDownCallback=buttonDownCallback,
            keyUpCallback=buttonUpCallback,
            keyHoldCallback=buttonHoldCallback,
            holdDelayTime=1,
            holdRepeatTime=0.1)

# Main Loop
while True:
    Matrix.update()