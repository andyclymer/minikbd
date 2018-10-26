# MiniKbd Software

When you connect the MiniKbd (or rather, the Adafruit Trinket M0) to your computer you'll find that it mounts as a small ``CIRCUITPY`` drive. Each time the Trinket M0 is powered up or restarted it will run the ``main.py`` that it finds at the root level of its file system, so all of your code editing will start with this file. I've included a few preset Python scripts in this area of the repo that you can drop in and start using.

The Trinket M0 is a full 32-bit computer, but resources are scarce! With only 256k of storage, after embedding a slimmed down Python standard library there isn't much room left for your own code. If you don't think you'll need to use the MiniKbd on a Windows computer, you can also save some space by deleting the Windows driver from the Trinket's drive.

## Sample code

Each of the directories in this part of the repo have sample code that you can drag and drop to the root level of the Trinket's file system. As soon as the new files show up, the device should reboot and it will be in use right away.

## Before editing

It might be really helpful to use the Terminal on your computer to connect to the device as a serial console, so that you can see any `print` statements and error messages while you work with the code on your MiniKBD. To do this, have a look at Adafruit's recommendation for [connecting to the serial console](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-mac-and-linux).
