number = int(input())
for x in range(number):
    string = input()
    list_1 = []
    count = -2
    for y in string:
        count += 1
        list_1.append(y)
    if len(string)>10:
        print(list_1[0]+str(count)+list_1[-1])
    else:
        print(string)