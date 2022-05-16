result = ""
command = int(input())
for i in range(command):
    number = int(input())
    string = str(number)
    array = []
    counter = 0
    for x in string:
        array.append(int(x))
    for y in range(len(array)):
        if array[y] != 0 and (number%array[y] == 0):
            counter += 1
    result += str(counter)+"\n"
print(result[:-1])