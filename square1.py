#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#Petit script python tout simple pour générer un carré de chiffres en lignes et en colonnes
#zf220811.1219

import sys

global currentNumber
global size
global square_size
global maxSquareSize


if __name__ == '__main__':
    print("Hello zuzu")

    if sys.argv[1] == "--size":
        try:
            size = int(sys.argv[2])
        except ValueError:
            print ("Not a number")
            exit()

print(size)

square_size = size * size
maxSquareSize = len(str(square_size))

print(square_size,maxSquareSize)

currentNumber = 1
while currentNumber <= square_size:
    for j in range(0,size):
        currentString = str(currentNumber).rjust(maxSquareSize, '0')
        print(currentString, "", end='', flush=True)
        currentNumber = currentNumber + 1
    print("")





