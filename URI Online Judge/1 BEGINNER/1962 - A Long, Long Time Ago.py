number = int(input())
while number >= 1:
    number2 = int(input())
    if number2 < 2015:
        result = 2015-number2
        print(result,"D.C.")
    else:
        result = number2-2014
        print(result,"A.C.")
    number -= 1