limit = int(input())
for x in range(limit):
    a,b,c = map(int,input().split())
    if abs(c-a) == abs(c-b):
        result = "Mouse C"
    elif abs(c-b) < abs(c-a):
        result = "Cat B"
    else:
        result = "Cat A"
    print(result)