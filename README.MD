Tips and Tricks
---------------

5/1/2014
Matthew Cahn
mcahn@princeton.edu


Using if __name__ == '__main__' so your module can be imported.

Documenting with doc strings so help() works.

Command line parsing with optparse (if you're using an older version of Python) (Python < 2.7).

    pyversion.py


Command line parsing.

    commandline1.py -- Using sys.argv directly -- BAD
    commandline2.py -- argparse (Python 2.7 or newer) -- define your options with code
    commandline3.py -- docopt (add-on module) -- define your options with documentation


Interleave two or more lists.

    zip.py


Produce a counter while iterating.

    enumerate.py


The built-in set type -- unions, intersections, etc.

    sets.py -- (Python >= 2.6)


List, dictionary, and set comprehensions -- a concise way to create these objects.

    comprehensions.py  -- (Python >= 3.0.0 for list, dictionary and set comprehensions)
                          (Python >= 2.0.0 -- list comprehensions only)


The dictionary setdefault method -- set the default value for a key, or return the current value.

The doctest module -- test a module according to the doc string.

Everything in Python is a reference.

    dictsAndDoctest.py


The Counter object in the collections module -- a customized dictionary for counting things.

    counter.py -- (Python >= 2.7)


Function argument passing -- positional, keyword, and variable number of arguments.

    arguments.py -- (Any Python version, but >= 3.0.0 for this particular example)


The logging module -- send messages to the screen, files, email, etc.

    loggingDemo.py
    loggingDemo.conf

Documentation:

    The Global Module index: docs.python.org

    The Python Cookbook: http://code.activestate.com/recipes/langs/python/

    docopt.org -- For the docopt module.