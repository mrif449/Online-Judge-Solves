limit = int(input())
for x in range(limit):
    number = int(input())
    list_1 = []
    for y in range(1,number):
        if number%y == 0:
            list_1.append(y)
    if sum(list_1) == number:
        print(number,"eh perfeito")
    else:
        print(number,"nao eh perfeito")