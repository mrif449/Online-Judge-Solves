for x in range(10):
    inp = int(input())
    if inp < 1:
        inp = 1
    result = f"X[{x}] = {inp}"
    print(result)