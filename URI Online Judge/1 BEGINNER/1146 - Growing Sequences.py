while True:
    inp = int(input())
    if inp == 0:
        break
    else:
        list_1 = []
        result = ""
        for x in range(1,inp+1):
            list_1.append(x) 
        for x in list_1:
            result += f"{x} "
        print(result[:-1])