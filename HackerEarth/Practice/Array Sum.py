number = int(input())
list_1 = list(map(int, input().split()))
sum = 0
for x in list_1:
    sum += x
print(sum)