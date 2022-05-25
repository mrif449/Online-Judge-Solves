result = ""
number = int(input())
for x in range(number):
    string = input()
    strings = []
    for y in string:
        if y not in strings:
            strings.append(y)
    strings.sort()
    if len(string) == 2:
        result += string[1] + "\n"
    else:
        result += strings[0] + "\n"
print(result[:-1])