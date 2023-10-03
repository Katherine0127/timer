"""
This program is for Nerve of Steel
timer.py is a simple Python script that will randomly set time between 5 and 25 seconds.
When the game begins, the program will display 'Players stand'.
Upon timer expiry, the program will display 'Time up. Last to sit down wins'.
timer.py uses the time library to help keep track of time
"""

print('Players stand')
# This program is timer that counts down

import random
import time # The time library has a sleep function that will pause the script for a specifized amount of time

set_time = int(random. randint(5, 25))

time.sleep(set_time)

print('Time up. Last to sit down wins')

