length = int(input())
array = list(map(int, input().split()))
array.sort()
array2 = []
for z in array:
    if z not in array2:
        array2.append(z)
unique = len(array2)
array3 = [1]*unique
idx = 0
for x in range(len(array)-1):
    if x<=length and array[x] == array[x+1]:
        array3[idx] += 1
        
    else:
        idx += 1
sum = 0
for y in array3:
    if y > 1:
        temp = y//2
        sum += temp
print(sum)