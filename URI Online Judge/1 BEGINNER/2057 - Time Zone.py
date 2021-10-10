a,b,c=list(map(int,input().split()))
sum = a+b+c
if sum>=24:
    sum -= 24
if sum<0:
    sum += 24
print(sum)