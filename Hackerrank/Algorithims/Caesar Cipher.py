number = int(input())
string = input()
char = int(input())
result = ""
for x in string:
    if 65<=ord(x)<=90:
        temp1 = (ord(x)+(char%26))
        if temp1 > 90:
            result += chr(temp1-26)
        else: result += chr(temp1)
    elif 97<=ord(x)<=122:
        temp = (ord(x)+(char%26))
        if temp>122:
            result+= chr(temp-26)
        else:
            result += chr(temp)
    else:
        result += x
print(result)