number = 0
inp = int(input())
while True:
    inp2 = int(input())
    if inp2 > inp:
        break
temp = inp
count = 1
while temp < inp2:
    temp += inp+count
    count += 1
print(count)