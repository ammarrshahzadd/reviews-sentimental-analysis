#!/usr/bin/env python3

import sys
import string

# Student ID: 0000000

# This combiner code just prints out what it receives
# and does not achieve anything at the moment but it
# can be used to just pass on data to the reducers.

# Use eprint to help debug your code and print out
# the contents of strings and lists without it being
# sent on to the reducer
def eprint(*args, **kwargs):
    print(args,file=sys.stderr,**kwargs)


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    print(line)
