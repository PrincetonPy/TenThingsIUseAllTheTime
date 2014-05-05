#!/bin/env python

'''

Example: Argument passing

Note that this example only works in Python version 3 only because it passes
*args and **kwargs to "print".  In Python 3, print is a function, but in
Python 2, print is a statement.
    
'''

def specifiedArgs(a, b, c, make=None, model=''):
    '''A function with positional and keyword arguments.'''

    print('specifiedArgs -- a: %s b: %s c: %s make: %s model: %s' % (a, b, c, make, model))
    
def myprint(*args, **kwargs):
    '''A function that can be called with any arguments.'''

    import datetime

    print('args: %s' % str(args))
    print('kwargs: %s' % kwargs)
    
    print(datetime.datetime.now())
    print(*args, **kwargs)

if __name__ == '__main__':

    # Call a function that takes specified arguments.
    specifiedArgs(1, 2, 3, model='Passat', make='VW')

    # Make arguments on the fly
    positionalArgs = (11, 12, 13)
    keywordArgs = {'make' : 'Subaru', 'model' : 'Outback'}

    specifiedArgs(*positionalArgs, **keywordArgs)

    myprint('abc', 7, 2.3, sep='|', end='\r\n')

