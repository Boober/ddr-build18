# Authors: Dexter, Nikolai, Oscar, Diego, Anja
# Build 18 Project 2018
# Virtual controller for DDR that handles the signals received from the
# Arduinos and converts them into keyboard presses.

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(2)

for char in "What time is it? Summer time.":
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(0.12)