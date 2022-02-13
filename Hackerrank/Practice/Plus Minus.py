counter1 = 0
counter2 = 0
counter3 = 0
positive = 0
negative = 0
zero = 0
number = int(input())
array = list(map(int, input().split()))
for x in array:
    if x < 0:
        negative += 1
    elif x == 0:
        zero += 1
    else:
        positive += 1
counter1 = "{:.6f}".format(positive/number)
counter2 = "{:.6f}".format(negative/number)
counter3 = "{:.6f}".format(zero/number)


print(counter1)
print(counter2)
print(counter3)