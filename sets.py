#!/bin/env python

'''

Example: The built-in set type

'''

import random

def randomWithReplacement(population, k):
    '''Return k random elements of population with replacement.'''
    
    nums = []
    for x in range(k):
        numList = random.sample(population, 1)
        nums.append(numList[0])

    return nums

if __name__ == '__main__':

    # Get two lists of 50 random numbers from 0 - 49

    nums1 = randomWithReplacement(range(50), 50)
    nums2 = randomWithReplacement(range(50), 50)

    # Get rid of the duplicates by putting them in sets.

    uniqueNumsSet1 = set(nums1)
    uniqueNumsSet2 = set(nums2)

    # Put the sets back in lists so they can be sorted.
    
    uniqueNumList1 = list(uniqueNumsSet1)
    uniqueNumList1.sort()
    uniqueNumList2 = list(uniqueNumsSet2)
    uniqueNumList2.sort()

    print('%d unique numbers in list 1.' % len(uniqueNumsSet1))
    print('set 1: %s' % uniqueNumList1)
    print('%d unique numbers in list 2.' % len(uniqueNumsSet2))
    print('set 2: %s' % uniqueNumList2)

    # Take the insection of the two sets
    intersection = uniqueNumsSet1.intersection(uniqueNumsSet2)
    intersectionList = list(intersection)
    intersectionList.sort()
    
    print('%d numbers common to both lists.' % len(intersection))
    print('Numbers in common: %s' % intersectionList)
