#!/bin/env python

'''

Example: A list comprehension is a concise syntax for creating a list.

'''

import sys

# This:

oddSquares = []
for x in range(10):
    if x % 2:
        oddSquares.append((x, x**2))

print(oddSquares)

# is equivalent to this:

oddSquares = [(x, x**2) for x in range(10) if x % 2]
     
print(oddSquares)

# You can also make a dictionary with a dict comprehension (Python 2.7 or newer)

oddSquares = {x: x**2 for x in range(10) if x % 2}

print(oddSquares)

# and a set with a set comprehension (Python 2.7 or newer)

oddSquares = {x**2 for x in range(10) if x % 2}

print(oddSquares)
