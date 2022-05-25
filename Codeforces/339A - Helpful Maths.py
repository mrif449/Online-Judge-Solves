result = ""
array = []
string = input().split("+")
for x in string:
    array.append(x)
array.sort()
for y in array:
    result += y+"+"
print(result[:-1])