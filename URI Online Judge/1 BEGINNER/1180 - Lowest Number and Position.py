limit = int(input())
list_1 = list(map(int, input().split()))
count = 0
postion = 0
lowest = list_1[0]
for x in list_1:
    if x<lowest:
        lowest = x
        postion = count
    count += 1
print("Menor valor:",lowest)
print("Posicao:",postion)