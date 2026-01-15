
from random import choice
import numpy as np
#notice that the jump of size |X_(n-2)| in positive or negative direction with even probability is just a jump of size X_(n-2) in positive or negative direction with even probability

#lowest X_50 could be is -2971215073
#highest X_50 could be is 12586269025
#so array needs 15557484098 cols

X = [0,1]

avg=0

P=[[0]*15557484098 for i in range(51)]
#2d array, where P[n][m] = Prob(X_n = m-2971215073)

P[0][2971215073]=1
P[1][2971215074]=1 #initial conditions

#here we fill in the probabilities, need to try make it efficient?
for n in range(2,51):
    for m in range(15557484098):
        min = next((i for i, x in enumerate(P[n]) if x != 0), None)
        max = next((i for i, x in enumerate(reversed(P[n])) if x != 0), None)
        for i in range(min, max+1):
            P[n][m] = P[n][m]+P[n-2][i]*(P[n-1][m-i]+P[n-1][m+i])

print(P[50])



"""   
for i in range(2, 51):
    direction = choice([-1,1])
    X.append(X[i-1]+abs(X[i-2])*direction)
    #avg+=X[5]
"""
    
print(X)

#print(avg/iterations)

#need a 2d array with the entry in [n,m] being P(X_n=m). Then work from there?
#need to look up the best way to showcase coding skills, and in what languages (multiple)
