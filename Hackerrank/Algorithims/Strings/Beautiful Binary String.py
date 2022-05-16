counter = 0
number = int(input())
string = input()
index = 0
for x in range(len(string)-1):
    if (index + 2) <= len(string)-1:
        character = string[index]+string[index+1]+string[index+2]
        if character == "010":
            counter += 1
            index += 3
        else:
            index += 1
print(counter)