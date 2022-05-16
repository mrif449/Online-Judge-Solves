result = ""
number = int(input())
for x in range(number):
    array = []
    string = input()
    for y in string:
        if y not in array:
            array.append(y)
    result += str(len(array))+"\n"
print(result[:-1])