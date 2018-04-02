# MiniKbd Hardware

![minikbd-oshpark-front](/images/minikbd-oshpark-front.png)

The MiniKbd is designed to be built in one of three configurations:

- “Six keyboard keyswitches”
- “Two rotary encoders”
- “One rotary encoder and two keyboard keyswitches”


## Parts List

Since there's more than one way to build the MiniKbd, not all component footprints on the MiniKbd PCB need to be filled depending on the variation you choose to build. Here are the parts lists for all three versions:

#### “Six Keyboard Keyswitches”
Part | Adafruit | Mouser | Tayda | Floris
--- |:---:|:---:|:---:|:---:
1 × Adafruit Trinket M0 | [#3500](https://www.adafruit.com/product/3500)  | [485-3500](https://www.mouser.com/ProductDetail/Adafruit/3500?qs=sGAEpiMZZMtw0nEwywcFgJjuZv55GFNm1yaWT2BHqYrZFoNRRhzyXg%3d%3d) | — | [#1947](https://www.floris.cc/shop/en/home/1947-adafruit-trinket-m0-for-use-with-circuitpython-arduino-ide.html)
6 × Keyswitches and keycaps (Cherry MX/ML, Kailh) _*(See note)_  | — | [Cherry MX](https://www.mouser.com/Electromechanical/Switches/_/N-5g2h?Keyword=cherry+mx&FS=True) | — | —
6 × 1N4148 Small Signal Diode | [#1641](https://www.adafruit.com/product/1641)  |  [512-1N4148](https://www.mouser.com/ProductDetail/ON-Semiconductor-Fairchild/1N4148?qs=sGAEpiMZZMudZehw8RjeZWbu6z6oTQTL)  | [A-157](https://www.taydaelectronics.com/1n4148-switching-signal-diode.html) | —

#### “Two Rotary Encoders”
Part | Adafruit | Mouser | Tayda | Floris
--- |:---:|:---:|:---:|:---:
1 × Adafruit Trinket M0 | [#3500](https://www.adafruit.com/product/3500)  | [485-3500](https://www.mouser.com/ProductDetail/Adafruit/3500?qs=sGAEpiMZZMtw0nEwywcFgJjuZv55GFNm1yaWT2BHqYrZFoNRRhzyXg%3d%3d) | — | [#1947](https://www.floris.cc/shop/en/home/1947-adafruit-trinket-m0-for-use-with-circuitpython-arduino-ide.html)
2 × Rotary Encoder (2-bit quadrature)  | [#377](https://www.adafruit.com/product/377) |  [PEC11R-4215F-S0024](https://www.mouser.com/ProductDetail/Bourns/PEC11R-4215F-S0024?qs=%2fha2pyFadujrq0cYyqrjqfzj8RH30yAAqLHU36uW%252bvgkXoG9QeJ4ZAKtmAuzI2d5)  | — | [#567](https://www.floris.cc/shop/en/knobs-buttons-joysticks/567-rotary-encoder-.html?search_query=encoder&results=12) _*(See note)_
2 × 33k resistors (1/8 watt) | — | **TK** | [A-3813](https://www.taydaelectronics.com/resistors/1-8w-metal-film-resistors/r-33k-ohm-1-8w-1-metal-film-resistor.html) | —
1 × 15k resistors (1/8 watt) | — | **TK** | [A-3803](https://www.taydaelectronics.com/resistors/1-8w-metal-film-resistors/r-15k-ohm-1-8w-1-metal-film-resistor.html) | —

#### “One rotary encoder and two keyboard keyswitches”
Part | Adafruit | Mouser | Tayda | Floris
--- |:---:|:---:|:---:|:---:
1 × Adafruit Trinket M0 | [#3500](https://www.adafruit.com/product/3500)  | [485-3500](https://www.mouser.com/ProductDetail/Adafruit/3500?qs=sGAEpiMZZMtw0nEwywcFgJjuZv55GFNm1yaWT2BHqYrZFoNRRhzyXg%3d%3d) | — | [#1947](https://www.floris.cc/shop/en/home/1947-adafruit-trinket-m0-for-use-with-circuitpython-arduino-ide.html)
2 × Keyswitches and keycaps (Cherry MX/ML, Kailh) _*(See note)_  | — | [Cherry MX](https://www.mouser.com/Electromechanical/Switches/_/N-5g2h?Keyword=cherry+mx&FS=True) | — | —
1 × Rotary Encoder (2-bit quadrature)  | [#377](https://www.adafruit.com/product/377) |  [PEC11R-4215F-S0024](https://www.mouser.com/ProductDetail/Bourns/PEC11R-4215F-S0024?qs=%2fha2pyFadujrq0cYyqrjqfzj8RH30yAAqLHU36uW%252bvgkXoG9QeJ4ZAKtmAuzI2d5)  | — | [#567](https://www.floris.cc/shop/en/knobs-buttons-joysticks/567-rotary-encoder-.html?search_query=encoder&results=12) _*(See note)_

## Notes on choosing parts

As always, if you wish to program the MiniKbd with Python, be sure that you purchase the black colored [Trinket M0](https://www.adafruit.com/product/3500) and *not* the blue colored Trinket 5v or 3.3v.

I went with a common “footprint” for the rotary encoder which you would find in the Bourns PEC11R series, but not all encoders out there will fit. Any encoders with a lighted shaft would have extra pins that won't fit on the MiniKbd circuit board. Also note that the rotary encoders from Floris have the correct footprint, however the shaft would be too short to fit with the enclosure. Also, don't forget to order a knob for the encoder, the recommended Bourns encoder would need a “D-shaft” knob.

There's an incredibly wide range of options when choosing keyswitches and keycaps, and the MiniKbd footprint works with the popular Cherry MX, Cherry ML and Kailh Low Profile keyswitches. You'll find a wide array of options for [different levels of force or clickyness](http://www.keyboardco.com/blog/index.php/2012/12/an-introduction-to-cherry-mx-mechanical-switches/), the best advice I have is to search around and order a few and see what you like. I prefer the [“Tactile Brown” Kailh Low Profile keyswitches from Novel Keys](https://novelkeys.xyz/products/kailh-low-profile-switches) and don't forget to order the [keycaps](https://novelkeys.xyz/collections/keycaps/products/kailh-low-profile-keycaps-blank). For the Cherry MX switches you have a wide range of options for keycaps from [Pimp My Keyboard](https://pimpmykeyboard.com/).


## Enclosure
*TK*


## Building it
*TK*
