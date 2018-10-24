# MiniKbd Software — Volume Control

For use with the “Two Rotary Encoders” build variation. One knob advances the track forward and back, the other knob adjusts the volume. This script builds off of the [TwoEncoderKeyboard](../TwoEncoderKeyboard) sample code.

On the Mac, turning the volume knob slowly increments the level with fine-grained control, the equivalent of holding down the “Option” key while pressing the volume keys on the keyboard. A quick turn increments the volume at a faster rate.

Pressing either knob will send the “Play/Pause” keystroke.

### How to use this sample code

Copy the `main.py` and `encoder.py` to the root level of your Trinket M0. The `main.py` code is run every time the Trinket reboots, and it imports code from the `encoder` library.

Before editing, I have some general advice for working with the MiniKBD one level back in the [Software](../) directory of this repo.
