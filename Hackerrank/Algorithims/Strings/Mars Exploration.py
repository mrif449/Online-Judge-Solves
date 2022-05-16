string = input()
length = int(len(string)/3)
matching = "SOS"*length
counter = 0
for x in range(len(string)):
    if string[x] != matching[x]:
        counter += 1
print(counter)