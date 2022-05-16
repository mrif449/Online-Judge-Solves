result = ""
number = int(input())
for x in range(number):
    array = []
    command = "NO\n"
    string1 = input()
    string2 = input()
    for y in string1:
        array.append(y)
    for z in array:
        if z in string2:
            command = "YES\n"
    result += command
print(result[:-1])