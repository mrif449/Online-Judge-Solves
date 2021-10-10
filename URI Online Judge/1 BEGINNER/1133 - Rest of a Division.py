number_1 = int(input())
number_2 = int(input())
number = number_1
if number_1 > number_2:
    number_1 = number_2
    number_2 = number
while number_1 < number_2:
    number_1 += 1
    if number_1%5 == 2 or number_1%5 == 3:
        if number_1 != number_2:
            print(number_1)