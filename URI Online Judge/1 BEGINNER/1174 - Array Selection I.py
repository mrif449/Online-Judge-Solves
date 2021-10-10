for x in range(100):
    number = float(input())
    if (number <= 10):
        number = "{:.1f}".format(number)
        x = str(x)
        print("A["+x+"] = "+number)