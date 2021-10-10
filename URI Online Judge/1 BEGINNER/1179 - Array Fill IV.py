even = []
odd = []
for x in range(15):
    inp = int(input())
    if inp%2 == 0:
        even.append(inp)
    else:
        odd.append(inp)
    if len(even) == 5:
        count = 0
        for y in even:
            result = f"par[{count}] = {y}"
            print(result)
            count += 1
        even = []
    if len(odd) == 5:
        count = 0
        for z in odd:
            result = f"impar[{count}] = {z}"
            print(result)
            count += 1
        odd = []
if len(odd) > 0:
    count = 0
    for a in odd:
        result = f"impar[{count}] = {a}"
        print(result)
        count += 1
if len(even) > 0:
    count = 0
    for b in even:
        result = f"par[{count}] = {b}"
        print(result)
        count += 1