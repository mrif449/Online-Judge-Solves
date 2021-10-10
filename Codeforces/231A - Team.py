count = 0
number = int(input())
for x in range(number):
    a,b,c = map(int,input().split())
    if a+b+c >= 2:
        count += 1
print(count)