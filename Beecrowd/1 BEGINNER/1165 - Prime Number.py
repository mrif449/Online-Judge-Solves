limit = int(input())
for x in range(limit):
    number = int(input())
    list_1 = []
    for y in range(1,number):
        if number%y == 0:
            list_1.append(y)
    if len(list_1) > 1:
        print(number,"nao eh primo")
    else:
        print(number,"eh primo")