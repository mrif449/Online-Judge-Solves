string = input()
result = ""
for x in range(len(string)):
    if x == 0 and ord(string[x]) >= 97:
        result += chr(ord(string[x])-32)
    else:
        result += string[x]
print(result)