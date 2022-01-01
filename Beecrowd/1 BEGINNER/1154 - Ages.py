data = []
while True:
    number = int(input())
    if number < 0:
        break
    else:
        data.append(number)
result = "{:.2f}".format(sum(data)/len(data))
print(result)