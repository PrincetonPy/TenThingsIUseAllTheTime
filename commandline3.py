#!/bin/env python

'''Usage: commandline3.py [-h] [-n NUM] <filename>

Example: Handling command-line arguments with docopt.

         The code is generated automatically from the documentation below.
         Requires additional installation: See docopt.org.

Arguments:
  filename

Options:
  -h, --help         show this help message and exit
  -n=<NUM>, --num=<NUM>  Specify a number [default: 3]

'''

if __name__ == '__main__':

    from docopt import docopt

    arguments = docopt(__doc__)
    print(arguments)
