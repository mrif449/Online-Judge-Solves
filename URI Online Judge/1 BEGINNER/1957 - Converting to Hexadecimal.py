def converter(number):
    integer = ["0"]*100
    count = 0
    while number != 0:
        store = 0
        store = number%16
        if store<10:
            integer[count] = chr(store+48)
            count += 1
        else:
            integer[count] = chr(store+55)
            count += 1
        number = int(number/16)
    counter = count-1
    while counter >= 0:
        print(integer[counter],end="")
        counter -= 1
inp = int(input())
converter(inp)
print()