x=[0,1]

while x[-1]<4000000:
    x.append(x[-1]+x[-2])

ans=0

for i in range(len(x)):
    if x[i]%2 == 0:
        ans=ans+x[i]

print(ans)