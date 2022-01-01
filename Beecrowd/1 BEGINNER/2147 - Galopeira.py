number = int(input())
for x in range(number):
    name = input()
    sum = len(name)
    result = "{:.2f}".format(sum/100)
    print(result)