num = int(input())
for x in range(num):
    string = input()
    sum = 0
    if string[0] != 0:
        for x in string:
            if x == "0":
                sum += 6
            elif x == "1":
                sum += 2
            elif x == "2":
                sum += 5
            elif x == "3":
                sum += 5
            elif x == "4":
                sum += 4
            elif x == "5":
                sum += 5
            elif x == "6":
                sum += 6
            elif x == "7":
                sum += 3
            elif x == "8":
                sum += 7
            elif x == "9":
                sum += 6
        print(sum,"leds")
    else:
        for x in string:
            if x == "0":
                sum += 6
            elif x == "1":
                sum += 2
            elif x == "2":
                sum += 5
            elif x == "3":
                sum += 5
            elif x == "4":
                sum += 4
            elif x == "5":
                sum += 5
            elif x == "6":
                sum += 6
            elif x == "7":
                sum += 3
            elif x == "8":
                sum += 7
            elif x == "9":
                sum += 6
        print(sum+6,"leds")