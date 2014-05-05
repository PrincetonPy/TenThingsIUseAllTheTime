#!/bin/env python

'''

Example: Interleave two (or more lists) with zip

Note: this is is not related to the Windows .zip file

'''

import itertools

# Interleave l1 and l2.  lMerged will be a list of two-tuples.

l1 = [1, 2, 3]
l2 = [11, 12, 13]

lMerged = zip(l1, l2)

print('l1: %s' % l1)
print('l2: %s' % l2)
print('lMerged: %s' % lMerged)

# Show how to iterate over the merged list.

for a, b in lMerged:
    print('a: %s b: %s' % (a, b))

# The same, but note that lMerged will be the length of the shortest list.

l1 = [1, 2, 3]
l2 = [11, 12, 13, 14, 15]

lMerged = zip(l1, l2)

print('l1: %s' % l1)
print('l2: %s' % l2)
print('lMerged: %s' % lMerged)

# Use itertools.izip_longest to grow the shorter list to the length of the longer list.

l1 = [1, 2, 3]
l2 = [11, 12, 13, 14, 15]

lMerged = itertools.izip_longest(l1, l2)

print('l1: %s' % l1)
print('l2: %s' % l2)
print('lMerged: %s' % list(lMerged))

