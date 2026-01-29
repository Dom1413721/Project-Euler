
A=[3,7,17] #list of numerators
B=[2,5,12] #list of denominators


for i in range(3,1000):
    A.append(2*A[i-1]+A[i-2]) #These are the recurrence relations for the numerators/denominators of this continued fraction
    B.append(2*B[i-1]+B[i-2])

ans=0

for i in range(1000):
    if len(str(A[i])) > len(str(B[i])):
        ans=ans+1

print(ans)

        