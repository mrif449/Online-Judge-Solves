array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
alice = 0
bob = 0
array3 = []
for x in range(len(array1)):
    array3.append(array1[x]-array2[x])
for x in array3:
    if x>0:
        alice += 1
    elif x<0:
        bob += 1
result = str(alice)+" "+str(bob)
print(result)