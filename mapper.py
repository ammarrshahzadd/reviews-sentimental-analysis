#!/usr/bin/env python3

import sys
import string

# Student ID: 0000000

# Use eprint to help debug your code and print out
# the contents of strings and lists without it being
# sent on to the combiner or reducer
def eprint(*args, **kwargs):
    print(args,file=sys.stderr,**kwargs)

# Remove common punctuation marks from a string
def removePunctuation(text):
    return text.translate(text.maketrans("","",".,!?()&'-"))

# Get a set of words from a file
def loadSet(filename):
    items = set()
    f = open(filename)
    for line in f:
	words = line.split()
	for word in words:
	    items.add(word)
    f.close()
    return items

# Start of the program
# Use 'loadSet' to load a list of keywords to look for
keywords = loadSet('keywords.txt')

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading, trailing whitespace and force to lower case
    line = line.strip().lower()
    #  Split up the line
    (title,review,rating) = line.split('\t')
    
    # Remove punctuation from the review 
    nopunc = removePunctuation(review)

    # Print out the rating and a count of 1
    # This is not the correct approach but
    # should give you a useful starting point
    print("%s\t%d" % (rating,1)) 
    
