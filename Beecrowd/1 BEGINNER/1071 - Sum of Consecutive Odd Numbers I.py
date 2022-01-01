X = int(input())
Y = int(input())
sum = 0
if X==Y:
    sum = 0
elif X<Y:
    for x in range(X,Y):
        if x % 2 != 0:
            sum += x
elif X>Y:
    for y in range(Y+1,X):
        if y % 2 != 0:
            sum += y
print(sum)