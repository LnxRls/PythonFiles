import os
import sys
import string
import math

from math import floor


def inputNumber(base):
    while True:
        try:
            base = int(input(base))
        except NameError:
            print("base value entered is NOT a integer")
            continue
        else:
            return base
            break


# creates master list of symbols
master_list = []
for i in range(0, 10):
    master_list.append(i)

master_list.extend(string.ascii_uppercase)

# gets the base from the user
base = inputNumber("please enter a base of destination numerical system: ")
numb = inputNumber("please enter number to convert: ")

# converts a decimal # to any other base numeric system
base_symbols = master_list[:base]
powerStr = ''

start = base-1
if base < 8:
    start = int(floor(math.log(numb)/math.log(base)))

for j in range(start, -1, -1):    # ranges from base-1 down to 0, e.g., for base=16 will range from 15 to 0
    power = numb//(base**j)
    powerStr = powerStr + str(base_symbols[power])
    numb = numb % (base**j)

print(powerStr)
