#!/bin/env python

'''

Example: if __name__ == '__main__':

You can import this module from elsewhere:
import main
and use any of it's functions:
main.f()

but you can also run it:
python main.py
'''

def f():
    print('A function in a module')

if __name__ == '__main__':
    print('Things to do only if I run this module')

    f()

    
