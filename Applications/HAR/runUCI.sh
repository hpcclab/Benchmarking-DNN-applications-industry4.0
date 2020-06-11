#!/bin/sh

END=30
## print date five times ##
x=$END 
while [ $x -gt 0 ]; 
do 
  python3 UCI_ANN.py
  x=$(($x-1))
done
