#!/bin/python3

import math

sum_lists = []

def append_list(lis, list_of_lists):
    return [lis+x for x in list_of_lists]

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
    
def power_sum2(X,N,pos):
    if X == 1:
        if pos == 1:
            return [[1]]
        else:
            return []
    elif X in (2,3):
        return []

    sq = int(math.floor(X**(1.0/N)))+1
    
    power_sum_lists = []
    while pos<=sq: 
        if X - pos**N > 0:
            #print("here "+str(n-fib_list_to_n[i]))
            power_sum_lists += append_list([pos],power_sum2(X - pos**N,N,pos+1))

        elif X - pos**N == 0:
            #print("there")
            power_sum_lists.append([pos])
            
            #print(fibo_sum_lists)
        
        
        pos+=1   

    
    return power_sum_lists


if __name__ == '__main__':

    X = int(input())

    N = int(input())

    #print(powerSum(X, N, 1))
    power_sums = power_sum2(X, N, 1)
    print(len(power_sums))
   
    for p in power_sums:
        print(p)
  
    
