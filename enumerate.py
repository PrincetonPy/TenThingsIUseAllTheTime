#!/bin/env python

'''

Example: enumerate -- iterate over a list (or other iterable) and produce each element and a counter

'''

import random

# Get a list of 100 random numbers from 0 - 999

nums = random.sample(range(1000), 100)

# Print every 10th number

for count, x in enumerate(nums):
    if count % 10 == 0:
        print('count: %3d %s' % (count, x))
