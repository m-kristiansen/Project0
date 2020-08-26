import math
import numpy as np

def add(x, y):
    return x+y

def factorial(x):
    y = 1
    if x == 0:
        y = 1
    elif x <0:
        exit()
    elif x > 0:
        for i in range(1, x+1):
            y = y*i
    return y

def sin(x):
    n = 10
    y = 0
    for i in range(n+1):
        y += (((-1)**i)*x**(2*i+1))/factorial((2*i+1))
    return y

def divition(x,y):
    return x/y

def times(x,y):
    return x*y

def power(x,y):
    return np.exp(y*np.log(x))
