number = int(input())
array = list(map(int, input().split()))
highest = []
lowest = []
high = array[0]
low = array[0]
standard = array[0]
for x in array:
    if x > high and x not in highest:
        high = x
        highest.append(x)
    elif x < low and x not in lowest:
        low = x
        lowest.append(x)
number1 = len(highest)
number2 = len(lowest)
result = str(number1)+" "+str(number2)
print(result)