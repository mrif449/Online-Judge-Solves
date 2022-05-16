string = input()
counter = 1
for x in range(1,len(string)):
    if string[x].isupper():
        counter += 1
print(counter)