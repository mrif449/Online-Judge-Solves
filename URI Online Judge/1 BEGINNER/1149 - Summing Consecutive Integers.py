temp = " "
number = 0
count = 0
list_1 = list(map(int,input().split()))
for x in list_1:
    if temp == " ":
        temp = x
    else:
        if x>0:
            number = x
            break
for y in range(number):
    count += temp
    temp += 1
print(count)