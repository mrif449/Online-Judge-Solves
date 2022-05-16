arr = list(map(int, input().split()))
max_list = []
min_list = []
minimum = arr[0]
maximum = arr[0]
unique = []
for a in arr:
    if a not in unique:
        unique.append(a)
if len(unique)  < 2:
    print(unique[0]*4,unique[0]*4)
else:
    for x in arr:
        if x < minimum:
            minimum = x
        if x> maximum:
            maximum = x
    for y in arr:
        if y != minimum:
            max_list.append(y)
        if y != maximum:
            min_list.append(y)
    result1 = (sum(min_list))
    result2 = (sum(max_list))
    print(result1,result2)