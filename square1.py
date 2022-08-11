#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#Petit script python tout simple pour générer un carré de chiffres en lignes et en colonnes
#zf220811.1516

import sys

global currentNumber
global size
global square_size
global maxSquareSize

if __name__ == '__main__':
    print("Soit un square de ", end='', flush=True)

    if sys.argv[1] == "--size":
        try:
            size = int(sys.argv[2])
        except ValueError:
            print ("Not a number")
            exit()

    print(size)
    print("")

    square_size = size * size
    maxSquareSize = len(str(square_size))
    
    def horizontal(size):
        currentNumber = 1
        while currentNumber <= square_size:
            for j in range(0,size):
                currentString = str(currentNumber).rjust(maxSquareSize, '0')
                print(currentString, "", end='', flush=True)
                currentNumber = currentNumber + 1
            print("")
 
    def vertical(size):
        currentLine = 1
        currentNumber = 1
        while currentLine <= size:
            for j in range(0,size):
                currentString = str(currentNumber).rjust(maxSquareSize, '0')
                print(currentString, "", end='', flush=True)
                currentNumber = currentNumber + size
            print("")
            currentLine = currentLine + 1
            currentNumber = currentLine

    horizontal(size)
    print("")
    vertical(size)



