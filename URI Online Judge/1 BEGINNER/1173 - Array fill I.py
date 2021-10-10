number = int(input())
result = f"N[0] = {number}"
print(result)
for x in range(1,10):
    number *= 2
    result_2 = f"N[{x}] = {number}"
    print(result_2)