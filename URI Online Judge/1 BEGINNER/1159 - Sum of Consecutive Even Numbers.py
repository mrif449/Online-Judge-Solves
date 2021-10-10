while True:
    inp = int(input())
    if inp == 0:
        break
    else:
        if inp%2 == 0:
            list_1 = []
            count = inp
            while len(list_1) < 5:
                list_1.append(count)
                count += 2
            print(sum(list_1))
        else:
            list_2 = []
            count = inp + 1
            while len(list_2) < 5:
                list_2.append(count)
                count += 2
            print(sum(list_2))