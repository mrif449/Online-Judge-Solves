limit = int(input())
for x in range(limit):
    a,b,c,d = map(float,input().split())
    count = 0
    while (a <= b):
        year_1 = int((a * (c / 100)))
        year_2 = int((b * (d / 100)))
        count += 1
        a += year_1
        b += year_2
        if (count > 100):
            break
    if (count > 100):
        print("Mais de 1 seculo.")
    else:
        print(count,"anos.")


""""
limit = int(input())
for x in range(limit):
    a,b,c,d = map(float,input().split())
    count = 0
    while True:
        if a != b:
            a = a+((a*c)/100)
            b = b+((b*d)/100)
            count+=1
        else:
            break    
        count += 1
    if count > 10:
        print("Mais de 1 seculo.")
    else:
        print(count,"anos.")
"""