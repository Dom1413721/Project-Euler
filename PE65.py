

A=[2,3,8] #list of numerators
B=[1,1,3] #list of denominators

CFe = [2,1]

for i in range (3,102):
    if i%3 == 0:
        CFe.append(i*2/3)
    else:
        CFe.append(1) 

for i in range(3,101):
    A.append(CFe[i]*A[i-1]+A[i-2])

def SumDigits(n):
    ans = 0
    while n >= 1:
        ans += n % 10
        n //= 10
    return ans

print(SumDigits(A[98]))

