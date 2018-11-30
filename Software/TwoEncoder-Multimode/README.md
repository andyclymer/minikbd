# MiniKbd Software — Multimode

This demo shows one way to use the Two Encoder build of the MiniKbd in more than one mode.

A more detailed breakdown of how the Two Encoder code works can be found with the TwoEncoder-Keyboard example, I would recommend becoming familiar with that demo first.

Pressing the left encoder button switches between modes. Each mode lights the RGB LED in a different color, and the callbacks are then written to fire off different keyboard combinations depending on the mode.

In this example, the first mode lights the LED greenish-blue and makes the encoder dials work as audio controls. The second mode lights the LED red and changes the encoders to work as shortcuts for a separate application.