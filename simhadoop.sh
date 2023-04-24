#!/usr/bin/env bash

cat 5.txt | ./mapper.py > mapout.txt
cat mapout.txt | ./combiner.py > comout.txt 
sort comout.txt | ./reducer.py > results.txt