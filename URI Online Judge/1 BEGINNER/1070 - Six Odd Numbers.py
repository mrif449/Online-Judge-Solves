x = int(input())
b = x+1
list1 = []
while len(list1)<6:
        if x%2 != 0:
            list1.append(x)
        else:
            list1.append(b)
        x+= 2
        b += 2
for a in list1:
    print(a)