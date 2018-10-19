# MiniKbd Software

When you connect the MiniKbd (or rather, the Adafruit Trinket M0) to your computer you'll find that it mounts as a small ``CIRCUITPY`` drive. Each time the Trinket M0 is powered up or restarted it will run the ``main.py`` that it finds at the root level of its file system, so all of your code editing will start with this file. I've included a few preset Python scripts in this area of the repo that you can drop in and start using.

The Trinket M0 is a full 32-bit computer, but resources are scarce! With only 256k of storage, after embedding a slimmed down Python standard library there isn't much room left for your own code. If you don't think you'll need to use the MiniKbd on a Windows computer, you can also save some space by deleting the Windows driver from the Trinket's drive.

## Updating CircuitPython

Before you get too far you will most likely need to update the version of CircuitPython that comes on the Trinket M0.

To update CircuitPython, you can follow [the updating instructions provided by Adafruit](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython), or follow my summary here —

* Go to the [latest release page on the CircuitPython repository](https://github.com/adafruit/circuitpython/releases/latest)
* Locate and download the build for the Trinket M0, its file name will look something like:
  * ``adafruit-circuitpython-trinket_m0-?.?.?.uf2``
* Connect the Trinket to your computer with a USB cable, if it wasn't already.
* On the Trinket you'll find a small "Reset" button, tap this button twice to make it reboot into the bootloader.
* A new "TRINKETBOOT" drive will mount on your desktop — simply copy the file you downloaded in a previous step onto this drive to install.
* The Trinket will reboot once again, this time with the latest version of CircuitPython.

After updating, you may also need to update some of the code libraries in the "lib" folder. Download the entire [bundle of Adafruit libraries](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/) for the version of CircuitPython that you just installed, and replace the older libraries with what you find here.

## Sample code

Each of the directories in this part of the repo have sample code that you can drag and drop to the root level of the Trinket's file system. As soon as the new files show up, the device should reboot and it will be in use right away.

## Before editing

It might be really helpful to use the Terminal on your computer to connect to the device as a serial console, so that you can see any `print` statements and error messages while you work with the code on your MiniKBD. To do this, have a look at Adafruit's recommendation for [connecting to the serial console](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-mac-and-linux).
