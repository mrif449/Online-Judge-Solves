limit = int(input())
for a in range(limit):
    a,b = map(int,input().split())
    list_1 = []
    if a% 2 != 0:
        while True:
            if len(list_1) == b:
                break
            else:    
                list_1.append(a)
            a += 2
        print(sum(list_1))
    else:
        c = a+1
        while True:
            if len(list_1) == b:
                break
            else:    
                list_1.append(c)
            c += 2
        print(sum(list_1))