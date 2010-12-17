#!/bin/sh 

# First argument is the number, prints the result in haskell and then in python

ghc --make $1
echo "Haskell solution:"
./$1
echo "Python solution:"
python "$1.py"