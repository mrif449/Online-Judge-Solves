number = int(input())
count = 0
for x in range(1000):
    result = f"N[{x}] = {count}"
    print(result)
    count += 1
    if count == number:
        count = 0