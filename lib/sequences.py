#!/usr/bin/env python3

def print_fibonacci(length):
    if(length==0):
        print([])
    elif(length==1):
        print([0])
    else:
        fib=[0,1]
        for i in range(length-2):
            fib.append(fib[-1] + fib[-2])
        print(fib)
print_fibonacci(0)