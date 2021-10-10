result = []
number = int(input())
for x in range(1,number+1):
    if number%x == 0:
        result.append(x)
for y in result:
    print(y)