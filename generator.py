from random import random
import itertools
import math as m

def chk(x):
    if any(x % div == 0 for div in range(2, x)):
        return True
    return False

def primes():
    p = 1
    while [True]:
        p += 1
        if (m.factorial(p-1)+1) % p == 0: yield p

print(list(itertools.takewhile(lambda x : x < 5, primes())))

# a = [i for i in range(5)][1:]
a = list(i+1 for i in range(4))
print(a)