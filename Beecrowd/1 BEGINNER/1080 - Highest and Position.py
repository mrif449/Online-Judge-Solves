highest = 0
for x in range(100):
    number = int(input())
    if number > highest:
        highest = number
        count = x+1
print(highest)
print(count)