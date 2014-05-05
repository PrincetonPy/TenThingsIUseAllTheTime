#!/bin/env python

'''
Check the python version.

Example: Use "if __name__ == '__main__':" above code that should
         only execute if you run the module, and not when you
         import the module.

         Put documentation in quotes at the top of the module
         and at the tops of functions.  Then help() works.
         
You can import this module from elsewhere:

import pyversion

and use it's functions:

pyversion.check(required)
pyversion.version()

and you can also run it:

python pyversion.py x.y.z
'''

# print('__name__ is: "%s"' % __name__)

import sys

def atleast(required):
    '''Return True if the Python version is at least the version
    given by required, otherwise False.

    required is a three-tuple, e.g. (2, 7, 0).'''

    return sys.version_info[:3] >= required

def version():
    '''Return the Python version as a string.'''
    
    return '.'.join(['%d' % num for num in sys.version_info[:3]])

# Only do these things when the module is run, not when it is imported.

if __name__ == '__main__':
    '''Check the Python version and display it.'''

    usage = '''usage: %prog x.y.z'''

    from optparse import OptionParser
    parser = OptionParser(usage=usage)
    options, args = parser.parse_args()

    if len(args) != 1:
        parser.error('You must specify the version to check, e.g. "3.1.0"')

    versionArg = args[0]
    
    versionTuple = tuple([int(x) for x in versionArg.split('.')])

    print('Am I running at least %s? %s' % (versionArg, atleast(versionTuple)))

    print('I am running %s' % version())
    
    
    
