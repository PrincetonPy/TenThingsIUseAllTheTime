#!/bin/env python

'''

Example: Interleave two (or more lists) with zip

Note: this is is not related to the Windows .zip file

'''

l1 = [1, 2, 3]
l2 = [11, 12, 13, 14]

lMerged = zip(l1, l2)

print('l1: %s' % l1)
print('l2: %s' % l2)
print('lMerged: %s' % lMerged)

for a, b in lMerged:
    print('a: %s b: %s' % (a, b))
