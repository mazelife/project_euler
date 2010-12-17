#!/bin/sh 

# First argument is the number, prints the result in haskell and then in python
echo ""
ghc --make $1
echo "----------------------------"
echo "Haskell solution:"
start="$(date +%s)"
./$1
stop="$(date +%s)"
echo ""
echo "Took" $(expr $stop - $start) "seconds in Haskell"
echo "----------------------------"
echo "Python solution:"
start="$(date +%s)"
python "$1.py"
stop="$(date +%s)"
echo ""
echo "Took" $(expr $stop - $start) "seconds in Python"