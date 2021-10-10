x = "huguinho"
y = "zezinho"
z = "luisinho"

a,b,c = map(int,input().split())
list_1 = [a,b,c]
list_2 = [a,b,c]
list_2.sort()
count = 0
for i in list_1:
    if list_2[1] != i:
        count += 1
    else:
        break
if count == 0:
    print(x)
elif count == 1:
    print(y)
elif count == 2:
    print(z)