result = ""
number = int(input())
for x in range(number):
    temp = 0
    string = input()
    palindrome = string[::-1]

    if string == palindrome:
        result += str(0)+"\n"
    else:
        string2 = string[::-1]
        array1 = []
        array2 = []
        temp = 0
        for y in string:
            array1.append(ord(y))
        for z in string2:
            array2.append(ord(z))
        for a in range(len(array1)):
            temp += abs(array1[a]-array2[a])
        result += str(int(temp/2))+"\n"
print(result[:-1])