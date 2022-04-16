result = ""
number = int(input())
for x in range(number):
    string = input()
    array1 = []
    array3 = []
    array4 = []
    for y in string:
        array1.append(ord(y))
    for a in range(1,len(array1)):
        array3.append(abs(array1[a-1]-array1[a]))
    array1.reverse()
    for b in range(1,len(array1)):
        array4.append(abs(array1[b-1]-array1[b]))
    if array3 == array4:
        result += "Funny\n"
    else:
        result += "Not Funny\n"
print(result[:-1])