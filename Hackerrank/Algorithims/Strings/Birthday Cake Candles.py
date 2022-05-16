limit = int(input())
list1 = list(map(int, input().split()))
highest = list1[0]
highest_list = []
for x in list1:
    if x > highest:
        highest = x
for y in list1:
    if y == highest:
        highest_list.append(y)
print(len(highest_list))