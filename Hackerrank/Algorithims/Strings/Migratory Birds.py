number = int(input())
array = list(map(int, input().split()))
highest = array[0]
lowest = array[0]
for x in array:
    if x > highest:
        highest = x
hashtable = [0]*(highest+1)
for y in array:
    hashtable[y] += 1
hashtable.pop(0)
much = hashtable[0]
less = hashtable[0]
for i in hashtable:
    if i > much:
        much = i
    answer1 = hashtable.index(much)
for j in hashtable:
    if j < less:
        less = j
    answer2 = hashtable.index(less)
counter = 0
for a in hashtable:
    if a == much:
        counter += 1
if counter == 1:
    print(answer1+1)
else:
    for b in range(len(hashtable)):
        if hashtable[b] == much:
            answer = hashtable.index(much)+1
            break
    print(answer)