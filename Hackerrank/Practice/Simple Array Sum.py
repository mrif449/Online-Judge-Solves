number = int(input())
sum = 0
array = list(map(int, input().split()))
for x in array:
    sum += x
print(sum)