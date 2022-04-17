result = ""
number = int(input())
for x in range(number):
    string = input()
    counter = 0
    for y in range(1,len(string)):
        if string[y-1] == string[y]:
            counter += 1
    result += str(counter)+"\n"
print(result[:-1])