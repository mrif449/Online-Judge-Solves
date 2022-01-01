sum = 0
X = int(input())
Y = int(input())
if X<Y:
    for a in range(X,Y+1):
        if a%13 != 0:
            sum += a
else:
    for b in range(Y,X+1):
        if b%13 != 0:
            sum += b
print(sum)