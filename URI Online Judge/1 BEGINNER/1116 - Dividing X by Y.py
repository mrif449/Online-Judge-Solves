num = int(input())
for x in range(num):
    a,b = map(int,input().split())
    if a == 0:
        print(0.0)
    elif b == 0:
        print("divisao impossivel")
    else:
        print("{:.1f}".format(a/b))