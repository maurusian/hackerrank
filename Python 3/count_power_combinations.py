#!/bin/python3

import math

def powerSum(X, N, pos):
    if X == 1:
        if pos == 1:
            return 1
        else:
            return 0
    elif X in (2,3):
        return 0
    else:
        sq = int(math.floor(X**(1.0/N)))
        counter = 0
        #must add one to sq because ** is inaccurate for integer powers
        #any excess will be handled in the else block anyway
        while pos <= sq+1: 
            
            if (X -  pos**N) == 0:
                counter+=1
            elif (X -  pos**N) > 0:
                counter+=powerSum((X - pos**N), N, pos+1)
            else:
                return counter
            
            pos+=1

        return counter

if __name__ == '__main__':

    X = int(input())

    N = int(input())

    result = powerSum(X, N, 1)
    
    print(result)
