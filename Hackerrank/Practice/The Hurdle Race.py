a,b = map(int,input().split())
array = list(map(int, input().split()))
highest = array[0]
for x in array:
    if x > highest:
        highest = x
result = highest-b
if result <= 0:
    print(0)
else:
    print(result)