#!/usr/bin/env python3
import sys

# Student ID: 0000000

# Use eprint to help debug your code and print out
# the contents of strings and lists without it being
# sent on to the combiner or reducer
def eprint(*args, **kwargs):
    print(args,file=sys.stderr,**kwargs)
  
# Given a dictionary of words and their associate counts,
# this function will return the word with the highest count
# and the count for that word.
def getMax(wordcounts):
    max = 0
    maxword = "?"
    for w in wordcounts:
        if wordcounts[w] > max:
            max = wordcounts[w]
            maxword = w
    return (maxword,max)
            
current_key = None
items = {}

# The code below does not solve the problem you have been
# given but it should help you see what the key and values
# the reducer is receiving and the order in which it arrives.
# You will need to make significant changes to this code to
# make it analyse your data and produce the correct output.

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from our mapper or combiner
    (key,values) = line.split('\t')
    
    items[key] = values
    
# Print out the contents of items
for i in items:
    # Print a string, a tab character and then another string
    print("%s\t%s" % (i,items[i]))
    
