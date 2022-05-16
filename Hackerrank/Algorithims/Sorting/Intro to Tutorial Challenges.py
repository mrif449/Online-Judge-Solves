number = int(input())
target = int(input())
array = list(map(int, input().split()))
counter = 0
for x in range(len(array)):
    if array[x] == number:
        break
    else:
        counter += 1
print(counter)