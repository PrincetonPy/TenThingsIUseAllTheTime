#!/bin/env python

'''

Example: Handling command-line arguments with argparse.

'''

import sys

if __name__ == '__main__':
    
    # argparse is new in Python 2.7
    # For Python 2.3 to 2.6, see optparse

    import pyversion
    if not pyversion.atleast((2, 7, 0)):
        print('The argparse module is new in Python 2.7.  You are running %s.' % pyversion.version())
        sys.exit(1)

    import argparse
    
    parser = argparse.ArgumentParser(description='Demonstrate command-line parsing.')

    parser.add_argument('-n', '--num', dest='num', default=3, help='Specify a number')

    parser.add_argument('filename')
    
    args = parser.parse_args()

    print('args.num: %s' % args.num)
    print('args.filename: %s' % args.filename)
