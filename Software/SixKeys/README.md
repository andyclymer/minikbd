# MiniKbd Software — Six Keyswitches

Edit the `buttonIDtoKeycode` dictionary in the `main.py` to customize the keyboard.

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
