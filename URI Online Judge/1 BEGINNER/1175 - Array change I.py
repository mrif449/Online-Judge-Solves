list_1 = []
for x in range(20):
    inp = int(input())
    list_1.append(inp)
count = 0
for y in list_1[::-1]:
    result = f"N[{count}] = {y}"
    print(result)
    count += 1