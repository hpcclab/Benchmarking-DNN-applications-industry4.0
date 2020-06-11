#!/bin/sh

END=30
## print date five times ##
x=$END 
while [ $x -gt 0 ]; 
do 
  python3 train.py --n_epoch 200
  x=$(($x-1))
done
