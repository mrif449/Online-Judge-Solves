while True:
    numbers = []
    a,b = map(int,input().split())
    if a <= 0 or b <= 0:
        break
    else:
        if(a > b):
            a, b = b, a
        for i in range(a, b + 1):
            numbers.append(i)
    result = 'Sum=%d'%sum(numbers)
    numbers.append(result)
    print(' '.join(map(str, numbers)))