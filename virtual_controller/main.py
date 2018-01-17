# Authors: Dexter, Nikolai, Oscar, Diego, Anja
# Build 18 Project 2018
# Virtual controller for DDR that handles the signals received from the
# Arduinos and converts them into keyboard presses.

#Requires python 2.7

#!python2

#If you have pip, need to do //pip install pynput// before this will work.
from pynput.keyboard import Key, Controller
import time

import bluetooth


	#Example Code for simulating key presses.#
keyboard = Controller()

#time.sleep(2)

#for char in "What time is it? Summer time.":
#	keyboard.press(char)
#	keyboard.release(char)
#	time.sleep(0.12)


	#End Example Code#


# simple inquiry example

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))