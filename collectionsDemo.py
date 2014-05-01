#!/bin/env python

'''

Example: The Counter and defaultdict objects in the collections module.

         (New in Python 2.7 and 2.5 respectively)
         
         Like dictsAndDoctest.py, but use Counter and defaultdict instead of a dictionaries.

         Counter is like a dictionary that assumes a value of 0 for missing items.
         defaultdict is a dictionary that uses a caller-supplied function to provide missing items.
         
The doctest module will test to see if the program produces this output:

>>> import dictsAndDoctest
>>> wordList = someWords.split()
>>> dictsAndDoctest.countWordsByLength(wordList)
Length:  4 Count: 1 Words: trod
Length:  5 Count: 3 Words: music, zinky, pekoe
Length:  6 Count: 2 Words: kozlov, pertly
Length:  7 Count: 4 Words: Valiant, canales, hotspur, brusher
Length:  8 Count: 5 Words: galoubet, Besancon, oxidizer, pargeted, pulpitum
Length:  9 Count: 5 Words: nonlegume, pretypify, dishallow, Intendant, ramillies
Length: 10 Count: 3 Words: earthmover, switchyard, spinaceous
Length: 11 Count: 2 Words: photometric, undercurved
Length: 12 Count: 3 Words: excruciation, hypoglobulia, nonbelieving
Length: 13 Count: 3 Words: dendritically, preenumerated, uncategorised
Length: 15 Count: 1 Words: prefermentation
Length: 17 Count: 1 Words: circumscriptively
'''

import collections
import sys

# From http://listofrandomwords.com

someWords = '''
Valiant excruciation photometric prefermentation nonlegume galoubet dendritically pretypify canales earthmover hotspur Besancon preenumerated oxidizer hypoglobulia kozlov uncategorised pertly music zinky dishallow brusher Intendant switchyard pekoe trod pargeted ramillies spinaceous nonbelieving pulpitum undercurved circumscriptively
'''

def countWordsByLength(words):
    '''Count the distribution of words by their lengths.'''
    
    # Make a histogram by word length.
    try:
        histogram = collections.Counter()
    except AttributeError:
        pyVersion = '.'.join(['%d' % num for num in sys.version_info[:3]])
        print('The Counter object is new in Python 2.7. You are running %s.' % pyVersion)
        sys.exit(1)
    # and make a list of words for each length.
    try:
        lengthLists = collections.defaultdict(list)
    except AttributeError:
        pyVersion = '.'.join(['%d' % num for num in sys.version_info[:3]])
        print('defaultdict is new in Python 2.5. You are running %s.' % pyVersion)
        sys.exit(1)

    # For every word:
    for word in words:
        wordLen = len(word)

        # Increment the histogram for this length
        histogram[wordLen] += 1
        # Add the word to the list for this length
        lengthLists[wordLen].append(word)
        
    allLengths = list(histogram.keys())
    allLengths.sort()

    for length in allLengths:
        print('Length: %2d Count: %d Words: %s' % (length, histogram[length], ', '.join(lengthLists[length])))

if __name__ == '__main__':

    # Verify that this program does what the __doc__ string says.
    import doctest
    doctest.testmod()

    # Split on spaces, create a list.
    wordList = someWords.split()
    
    countWordsByLength(wordList)
