num = int(input())
for x in range(num):
    number = int(input())
    if number == 0:
        print("NULL")
    elif number > 0 and number % 2 == 0:
        print("EVEN POSITIVE")
    elif number > 0 and number % 2 != 0:
        print("ODD POSITIVE")
    elif  number < 0 and number % 2 == 0:
        print("EVEN NEGATIVE")
    elif number < 0 and number % 2 != 0:
        print("ODD NEGATIVE")