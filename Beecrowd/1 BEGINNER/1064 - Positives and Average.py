positive = []
for x in range(6):
    num = float(input())
    if num > 0:
        positive.append(num)
sum = 0
for y in positive:
    sum += y
average = sum/len(positive)
result = "{:.1f}".format(average)

print(len(positive),"valores positivos")
print(result)