counter = 0
number = int(input())
for x in range(number):
    string = input()
    if "++" in string:
        counter += 1
    else:
        counter -= 1
print(counter)