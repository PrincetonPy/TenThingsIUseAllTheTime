#!/bin/env python

'''

Example: The Counter object in the collections module.

         (New in Python 2.7)
         
         Like dictsAndDoctest.py, but use a Counter for the histogram instead of a dictionary.

         The Counter is like a dictionary that assumes a value of 0 for missing items.
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

    # For every word:
    for word in words:
        wordLen = len(word)

        # Increment the histogram for this length
        histogram[wordLen] += 1
    
    maxLen = max(histogram.keys())

    for length in range(1, maxLen + 1):
        print('Length: %2d Count: %d' % (length, histogram[length]))

if __name__ == '__main__':

    # Split on spaces, create a list.
    wordList = someWords.split()
    
    countWordsByLength(wordList)
