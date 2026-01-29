from sympy import *
from functools import lru_cache

@lru_cache(None)
def isprime_cached(n):
    return isprime(n)

def isPrimeSet(x):
    isPrimeSet = True
    for i in range(len(x)):
        if isPrimeSet == False:
            break
        for j in range(i):
            if isPrimeSet == False:
                break
            if not(isprime_cached(int(str(x[i]) + str(x[j]))) and isprime_cached(int(str(x[j]) + str(x[i])))):
                #print(int(str(x[i]) + str(x[j])))
                #print(int(str(x[j]) + str(x[i])))
                isPrimeSet = False
                break

    return isPrimeSet

def FindUpperLimit(x):
    done=False
    for i in primerange(10**6-1,10**10):
        if done == True:
            break
        if isprime(i) and str(i)[-1] != 2 and str(i)[-1] != 5 and isPrimeSet(x+[i]):
            print(i)
            x.append(i)
            done = True
            break
    print(x)
    return(sum(x))

FindUpperLimit([3,7,109,673])
