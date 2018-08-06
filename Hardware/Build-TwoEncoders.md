# Build Doc — “Two Rotary Encoders” Configuration

![minikbd-oshpark-front](/images/two-encoder-enclosure.jpg)


## Parts List

Qty | Component | Note
:---:|---|---
1 | Adafruit Trinket M0 | *The black “M0” and not the blue “3V” or “5V” variations of the Trinket*
2 | Rotary Encoders | *2-bit quadrature, with a common footprint from the Bourns PEC11R series*
1 | 33kΩ Resistors | *1/8 watt*
2 | 15kΩ Resistors | *1/8 watt*
— | Various enclosure parts | *Optional but recommended, see notes below*

In this configuration, the only components to add to the circuit board are highlighted below in blue. All other component footprints should be left unpopulated.

![minikbd](/Hardware/buildImages/footprint-twoencoders.gif)


### Prepare the Trinket M0
- The Trinket M0 comes packaged with a strip of pin headers. Start by clipping the header strip into two smaller sections of five pins. It's okay if there's a small strip of header left over after doing this.
- Solder the headers onto the Trinket. It might help to use a small prototyping breadboard to make sure the header pins are aligned upright and not at an angle.
- After attaching the headers, you might decide to clean things up a little bit by trimming the freshly soldered pins to be flush with the top of the Trinket board, and rounding off the freshly clipped solder joints by momentarily touching the soldering iron back to the roughly cut pin (as shown)

### Attach the Trinket to the MiniKbd board
- Fit the Trinket to the MiniKbd, being careful to orient the Trinket with its USB port facing out.
- Solder all 10 pins to the back of the MiniKbd, and clip the excess length of the pins flush with the bottom side of the board.

### Solder the resistors
- Three resistors are required to make the pushbuttons on the rotary encoders work.
- Take care to use the correct resistor values, R1 is a 33k resistor, while R2 and R3 are 15k resistors.
- It might help to place all the resistors in their positions and cover them with tape before flipping the board over and soldering, to keep them all neatly aligned.
- After soldering, clip the excess length of the resistor leads flush with the bottom side of the board.

### Add the Rotary Encoders
- The rotary encoders have two pins on one side (which connects their pushbutton), three pins on the other side (for the directional signal out of the encoder) and will usually have one more pin on the remaining sides to help hold the encoder firmly to the board.
- If you plan to use an enclosure with holes for the encoder shafts, it might be helpful to fit both encoders into the board and place the top of the enclosure over the shafts before soldering, to ensure that they'll fit properly once they're firmly soldered in place.
- Solder all of the encoder pins on the bottom side of the board, including the side pins that are there for stability. Clip the excess length of the pins to be flush with the board after soldering.

### Cleanup
- At this point the soldering is complete! Double check all of your soldering work to make sure that you didn't accidentally bridge two pins together with a blob of solder, and clip any remaining pins flush with the bottom of the board. If the pins aren't clipped flush with the board, the enclosure may not fit properly.
- Depending on the type of solder used, you may need to clean any remaining "flux" residue on your board. If you used a "no-clean" solder this is still a required step if you don't plan to put the MiniKbd in an enclosure, because after assembly is completely you should avoid coming into contact with the flux residue. Isporopyl alcohol ("rubbing alcohol") on a cotton swab or paper towel should be enough to clean off any residue, just be careful to not saturate the inner workings of your encoders or keyswitches with alcohol.

### Assemble the enclosure, or at least add the feet
- If you plan to use the MiniKbd without an enclosure, you will want to at least apply four rubber feet to the bottom of the board so that it sits firmly on your desktop as you use it, and so that the roughly cut pins on the bottom side don't scratch the surface.
- If you plan to build the recommended laser cut enclosure, have a look at the Enclosure page for assembly instructions.
