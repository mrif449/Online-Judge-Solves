a,b,c = map(int,input().split())
number = int(input())
array = list(map(int, input().split()))
counter =0
for x in array:
    if b<x<c:
        counter += 1
print(counter)