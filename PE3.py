import math

x=600851475143
factors=[1]


def LowestFactor(x):

    prime = True

    for i in range(2,math.floor(math.sqrt(x))):
        if x%i == 0:
            prime = False
            return i
            break
    
    if prime == True:
        return(x)

while x > 1:
    factors.append(LowestFactor(x))
    print(factors)
    x=x/int(factors[-1])

print(factors)
    