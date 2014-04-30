#!/bin/env python

'''

Example: How *not* to handle command-line arguments.

Usage:

    commandline1.py -a blah
    
'''

import sys

if __name__ == '__main__':

    if sys.argv[1] == '-a':
        aArg = sys.argv[2]
    else:
        aArg = None
        
    print('aArg: %s' % aArg)

 
