string = input()
array1 = []
for x in string:
    if x not in array1:
        array1.append(x)
array2 = [0]*len(array1)

end = len(string)
for y in range(len(array1)):
    for z in range(len(string)):
        if array1[y] == string[z]:
            array2[y] += 1

odd_counter = 0
for a in array2:
    if a%2 != 0:
        odd_counter += 1
if odd_counter > 1:
    print("NO")
else:
    print("YES")