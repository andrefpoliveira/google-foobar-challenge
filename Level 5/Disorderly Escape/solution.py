from math import factorial
from collections import Counter
from fractions import gcd

def cycle_counter(cycle, block):
    cycle_count=factorial(block)
    for a, b in Counter(cycle).items():
        cycle_count //= (a**b)*factorial(b)
    return cycle_count        

def combs(n, i=1):
    yield [n]
    for i in range(i, n//2+1):
        for p in combs(n-i, i):
            yield [i]+p

def solution(w, h, s):    
    grids=0
    for c_w in combs(w):
        for c_h in combs(h):
            print(c_h)
            cycle_count=cycle_counter(c_w, w)*cycle_counter(c_h, h)
            grids += cycle_count*(s**sum([sum([gcd(i, j) for i in c_w]) for j in c_h]))
              
    return str(grids // (factorial(w)*factorial(h)))
