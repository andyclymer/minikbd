# MiniKbd Hardware

![minikbd-oshpark-front](/images/minikbd-oshpark-front.png)

The MiniKbd is designed to be built in one of three configurations:

- “Six keyboard keyswitches”
- “Two rotary encoders”
- “One rotary encoder and two keyboard keyswitches”

## Buying it
Build one yourself! A batch of MiniKbd circuit boards is currently being made and once they've arrived in mid-April I'll have some for sale for around $6 each. Then, you can collect the parts listed below and build your own (or all three!)


## Parts List
Since there's more than one way to build the MiniKbd, not all component footprints on the MiniKbd PCB need to be filled depending on the variation you choose to build. Here are the parts lists for all three versions:

#### “Six Keyboard Keyswitches”
Qty | Component | Note
:---:|---|---
1 | Adafruit Trinket M0 | *The black “M0” and not the blue “3V” or “5V” variations of the Trinket*
6 | Keyswitches and keycaps | *Cherry MX, Cherry ML or Kailh Low Profile keyswitches will work*
6 | 1N4148 Small Signal Diodes | 
— | Various enclosure parts | *Optional but recommended, see notes below*


#### “Two Rotary Encoders”
Qty | Component | Note
:---:|---|---
1 | Adafruit Trinket M0 | *The black “M0” and not the blue “3V” or “5V” variations of the Trinket*
2 | Rotary Encoders | *2-bit quadrature, with a common footprint from the Bourns PEC11R series*
2 | 33kΩ Resistors | *1/8 watt*
1 | 15kΩ Resistors | *1/8 watt*
— | Various enclosure parts | *Optional but recommended, see notes below*

#### “One rotary encoder and two keyboard keyswitches”
Qty | Component | Note
:---:|---|---
1 | Adafruit Trinket M0 | *The black “M0” and not the blue “3V” or “5V” variations of the Trinket*
2 | Keyswitches and keycaps | *Cherry MX, Cherry ML or Kailh Low Profile keyswitches will work*
2 | 1N4148 Small Signal Diodes | 
1 | Rotary Encoder | *2-bit quadrature, with a common footprint from the Bourns PEC11R series*
— | Various enclosure parts | *Optional but recommended, see notes below*


## Buying Parts

#### Adafruit Trinket M0
The Trinket M0 can be purchased directly from the manufacturer, Adafruit, and can be found on other online shops for about $9 or €9. The most important consideration for this project is to buy the black colored Trinket “M0”, and *not* the blue “3V” or “5V” variations.

Retailer | Part number
---|---
Adafruit | Adafruit Trinket M0 [#3500](https://www.adafruit.com/product/3500)
Mouser | Adafruit Trinket M0 [485-3500](https://www.mouser.com/ProductDetail/Adafruit/3500?qs=sGAEpiMZZMtw0nEwywcFgJjuZv55GFNm1yaWT2BHqYrZFoNRRhzyXg%3d%3d)
Floris | Adafruit Trinket M0 [#1947](https://www.floris.cc/shop/en/home/1947-adafruit-trinket-m0-for-use-with-circuitpython-arduino-ide.html)


#### Keyswitches and keycaps
There's an incredibly wide range of options when choosing keyswitches and keycaps, and the MiniKbd footprint works with the popular Cherry MX, Cherry ML and Kailh Low Profile keyswitches. Do a little bit of research first, the popular Cherry MX switches come in a wide array of options for [different levels of force or clickyness](http://www.keyboardco.com/blog/index.php/2012/12/an-introduction-to-cherry-mx-mechanical-switches/). I think the best advice I have is to order a few and see what you like. I prefer the [“Tactile Brown” Kailh Low Profile keyswitches from Novel Keys](https://novelkeys.xyz/products/kailh-low-profile-switches) and don't forget to order the [keycaps](https://novelkeys.xyz/collections/keycaps/products/kailh-low-profile-keycaps-blank). For the Cherry MX switches you have a wide range of options for keycaps from [Pimp My Keyboard](https://pimpmykeyboard.com/).

Retailer | Part number
---|---
Novel Keys | [Kailh Low Profile Keyswitches](https://novelkeys.xyz/products/kailh-low-profile-switches) and [Kailh Low Profile Keycaps](https://novelkeys.xyz/collections/keycaps/products/kailh-low-profile-keycaps-blank)
Mouser | [Cherry MX search results](https://www.mouser.com/Electromechanical/Switches/_/N-5g2h?Keyword=cherry+mx&FS=True) with lots of options

#### 1N4148 Small Signal Diodes
An extremely common part, one diode is required for each keyswitch.

Retailer | Part number
---|---
Adafruit | [#1641](https://www.adafruit.com/product/1641) for a 10 pack
Mouser | [512-1N4148](https://www.mouser.com/ProductDetail/ON-Semiconductor-Fairchild/1N4148?qs=sGAEpiMZZMudZehw8RjeZWbu6z6oTQTL)
Tayda Electronics | [A-157](https://www.taydaelectronics.com/1n4148-switching-signal-diode.html) for 1¢ each!

#### Rotary Encoders
You will need a standard *2-bit quadrature* encoder, which means that with each click as you rotate it will send a [pattern of pulses on two pins](https://en.wikipedia.org/wiki/Rotary_encoder) (and not a “gray code” encoder which uses three pins). I went with a common “footprint” for the rotary encoder which you would find in the Bourns PEC11R series, but not all encoders out there will fit. Any encoders with a lighted shaft would have extra pins that won't fit on the MiniKbd circuit board. Also note that the rotary encoders from Floris have the correct footprint, however the shaft would be too short to fit with the enclosure, but it would work fine without the enclosure top. 

Retailer | Part number
---|---
Adafruit | [#377](https://www.adafruit.com/product/377) comes with a simple knob
Mouser |  [PEC11R-4215F-S0024](https://www.mouser.com/ProductDetail/Bourns/PEC11R-4215F-S0024?qs=%2fha2pyFadujrq0cYyqrjqfzj8RH30yAAqLHU36uW%252bvgkXoG9QeJ4ZAKtmAuzI2d5)
Floris | [#567](https://www.floris.cc/shop/en/knobs-buttons-joysticks/567-rotary-encoder-.html?search_query=encoder&results=12) will work but will be too short for the enclosure

Also, don't forget to order a knob for the encoder, the recommended Bourns encoder would need a “D-shaft” knob.

Retailer | Part number
---|---
Adafruit | [#2055](https://www.adafruit.com/product/2055) is a larger 35mm knob, it won't sit flush with the enclosure but still looks nice
Thonk | [Davies 1900h clone D-shaft](https://www.thonk.co.uk/shop/1900h-d/)
DJ Tech Tools | [Chroma Caps](https://store.djtechtools.com/products/chroma-caps-knobs-and-faders)


#### Resistors
The “Two Encoders” build will need three resistors, but the two other builds won’t require any. The smaller and very common 1/8 Watt metal film resistors will fit nicely.

Retailer | Part number
---|---
Tayda Electronics | [A-3813](https://www.taydaelectronics.com/resistors/1-8w-metal-film-resistors/r-33k-ohm-1-8w-1-metal-film-resistor.html) for the 33k ohm (×2), and [A-3803](https://www.taydaelectronics.com/resistors/1-8w-metal-film-resistors/r-15k-ohm-1-8w-1-metal-film-resistor.html) for the 15k ohm (×1)
Mouser | **TK**


#### Enclosure parts

The enclosure consists of a variety of pieces, all of which are optional or can be substituted:
- Laser cut parts from acrylic sheet
- 4 × 8mm long M3 sized standoffs (5 or 6mm long should work)
- 9 × M3x6mm screws
- 1 × M3 nut
- 5 × M3x1mm washers
- 4 × rubber bumper feet

The MiniKbd doesn't need to be built in an enclosure, but at minumum I would highly suggest at least getting a set of small rubber bumper feet for the bottom so that it stays put and doesn't scratch up your desk. [Adafruit has a set of four](https://www.adafruit.com/product/550) if you're already ordering from them, but I prefer the [3M SJ5312 Bumpon](https://www.amazon.com/gp/product/B000NG60SW/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1) because they're very small and grippy.

For the enclosure, I've laser cut parts in 1/8 inch (3mm) acrylic sheet, which can be avaialble from many sources. Files are available in the Enclosure folder of the repo. You won't want to completely obscure the LEDs on the top of the Trinket so I would recommend translucent acrylic if available. I like using the [Frosted Satin Ice](https://www.canalplastic.com/collections/plexi-sheets/products/0d010-df-frosted-satin-ice-acrylic-sheet?variant=32918342606) that I buy at Canal Plastics in NYC, but I would encourage you to look for local options. Laser cutting might also be able to be ordered from [Ponoko](https://www.ponoko.com/).

Amazon and Ebay seem to be good places to buy a variety of standoffs and screws at a resonable price, I use the [white Nylon m3 standoff assortment](https://www.amazon.com/gp/product/B01DK3905Y/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1) which is also available in [black](https://www.amazon.com/gp/product/B01E8JZWZ6/ref=ox_sc_sfl_title_14?ie=UTF8&psc=1&smid=A1Z1DJFHECM1GS), along with a small set of [M3 1mm nylon washers](https://www.amazon.com/gp/product/B01N45UFLG/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1). You can go nuts and get the same [stainless hex screws](https://www.amazon.com/gp/product/B01M3SFIAZ/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1) that I used for the top four screws of the enclosure.


## Building it
*Working on a build guide!*
