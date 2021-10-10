list_1 = []
inp = float(input())
for x in range(100):
    list_1.append(inp)
    floating = "{:.4f}".format(inp)
    result = f"N[{x}] = {floating}"
    print(result)
    inp = inp/2