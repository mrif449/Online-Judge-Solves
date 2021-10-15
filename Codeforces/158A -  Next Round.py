a,b = map(int,input().split())
list_1 = list(map(int, input().split()))
count = 0
temp = list_1[b-1]
for x in list_1:
    if x>=temp:
        if x>0:
            count += 1
print(count)