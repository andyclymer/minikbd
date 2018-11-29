# Build Doc — “One Rotary Encoder and Two Keyboard Keyswitches” Configuration

![minikbd](/images/two-key-enclosure.jpg)


## Parts List

Qty | Component | Note
:---:|---|---
1 | Adafruit Trinket M0 | *The black “M0” and not the blue “3V” or “5V” variations of the Trinket*
2 | Keyswitches and keycaps | *Cherry MX, Cherry ML or Kailh Low Profile keyswitches will work*
2 | 1N4148 Small Signal Diodes | 
1 | Rotary Encoder | *2-bit quadrature, with a common footprint from the Bourns PEC11R series*
— | Various enclosure parts | *Optional but recommended, see notes below*

In this configuration, the only components to add to the circuit board are highlighted below in blue. All other component footprints should be left unpopulated.

![minikbd](/Hardware/buildImages/footprint-oneencoder.gif)

### Solder the diodes

![Diodes](/Hardware/buildImages/small/parts-diodes.jpg)
![Diodes](/Hardware/buildImages/small/build-diodes-2.jpg)

- Each keyswitch is paired up with one diode. Since only two keyswitches are used, you only need to add diodes for "D1" and "D2".
- A diode is a directional component so its orientation on the board does matter. The "cathode" (or, negative) end of the diode will be marked with a contrasting color, usually black or white. It's important that you position the diode so that this stripe is at the same side as the stripe and triangle as marked on the board. 

![Diodes](/Hardware/buildImages/diodes-footprint.jpg)

- The other side of the diode, the "anode" end, can go through either of the two remaining holes on the board. The extra hole is there for diodes that are too long to fit in the smaller set of holes.
- It might help to place all diodes in their positions and cover them with tape before flipping the board over and soldering. This will help keep them all neatly aligned.
- After soldering, clip the excess length of the diode leads flush with the bottom side of the board.

### Prepare the Trinket M0

![Trinket](/Hardware/buildImages/small/parts-trinket.jpg)

- The Trinket M0 comes packaged with a strip of pin headers. Start by clipping the header strip into two smaller sections of five pins. It's okay if there's a small strip of header left over after doing this.

![Trinket](/Hardware/buildImages/small/parts-trinket-proto.jpg)

- Solder the headers onto the Trinket. It might help to use a small prototyping breadboard to make sure the header pins are aligned upright and not at an angle.

![Trinket](/Hardware/buildImages/small/parts-trinket-headers.jpg)

- After attaching the headers, you might decide to clean things up a little bit by trimming the freshly soldered pins to be flush with the top of the Trinket board, and rounding off the freshly clipped solder joints by momentarily touching the soldering iron back to the roughly cut pin (as shown)

### Attach the Trinket to the MiniKbd board

- Fit the Trinket to the MiniKbd, being careful to orient the Trinket with its USB port facing out.
- Solder all 10 pins to the back of the MiniKbd, and clip the excess length of the pins flush with the bottom side of the board.

### Connect the keyswitches
- All of the recommended styles of keyswitches will only have two pins, but you will notice that each position on the MiniKbd was designed to have holes for many popular types of keyswitches. Rotate your keyswitch until it lines up with the holes provided but don't force it if you aren't certain that it's lined up correctly. The recommended "Kailh Low-Profile" switches have two plastic pins which should fit firmly in two support holes on the board, so they might take a little bit of pressure to fit, but only press them in firmly if you're sure the keyswitch pins aren't being forced into the wrong holes.
- If the keyswitch is loose, you may need to temporarily tape it to the board before turning it over and soldering.
- I would recommend soldering only one of the two pins at first, checking to make sure that the keyswitch still appears to be aligned correctly before soldering the second pin.

### Add the Rotary Encoder
- The rotary encoder has two pins on one side (which connects the pushbutton), three pins on the other side (for the directional signal out of the encoder) and will usually have one more pin on the remaining sides to help hold the encoder firmly to the board.
- If you plan to use an enclosure with holes for the encoder shafts, it might be helpful to fit the encoder into the board and place the top of the enclosure over the shaft before soldering, to ensure that they'll fit properly once they're firmly soldered in place.
- Solder all of the encoder pins on the bottom side of the board, including the side pins that are there for stability. Clip the excess length of the pins to be flush with the board after soldering.

### Cleanup
- At this point the soldering is complete! Double check all of your soldering work to make sure that you didn't accidentally bridge two pins together with a blob of solder, and clip any remaining pins flush with the bottom of the board. If the pins aren't clipped flush with the board, the enclosure may not fit properly.
- Depending on the type of solder used, you may need to clean any remaining "flux" residue on your board. If you used a "no-clean" solder this is still a required step if you don't plan to put the MiniKbd in an enclosure, because after assembly is completely you should avoid coming into contact with the flux residue. Isporopyl alcohol ("rubbing alcohol") on a cotton swab or paper towel should be enough to clean off any residue, just be careful to not saturate the inner workings of your encoders or keyswitches with alcohol.

### Assemble the enclosure, or at least add the feet
- If you plan to use the MiniKbd without an enclosure, you will want to at least apply four rubber feet to the bottom of the board so that it sits firmly on your desktop as you use it, and so that the roughly cut pins on the bottom side don't scratch the surface.
- If you plan to build the recommended laser cut enclosure, have a look at the Enclosure page for assembly instructions.
