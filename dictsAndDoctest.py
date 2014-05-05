#!/bin/env python

'''

Example: 1) The dictionary setdefault method

         2) The doctest module.

         3) Everything is a reference
         
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

# From http://listofrandomwords.com

someWords = '''
Valiant excruciation photometric prefermentation nonlegume galoubet dendritically pretypify canales earthmover hotspur Besancon preenumerated oxidizer hypoglobulia kozlov uncategorised pertly music zinky dishallow brusher Intendant switchyard pekoe trod pargeted ramillies spinaceous nonbelieving pulpitum undercurved circumscriptively
'''

def countWordsByLength(words):
    '''Count the distribution of words by their lengths.'''

    # Make a histogram by word length,
    # and make a list of words for each length.
    histogram = {}
    lengthLists = {}

    # For every word:
    for word in words:
        wordLen = len(word)
        
        # Increment the histogram for this length
        lengthCount = histogram.setdefault(wordLen, 0)
        lengthCount += 1
        histogram[wordLen] = lengthCount

        # Add the word to the list for this length
        l = lengthLists.setdefault(wordLen, [])
        l.append(word)
        # l is a reference to the list so we're done

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
