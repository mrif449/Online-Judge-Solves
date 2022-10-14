a,b = map(int,input().split())
array = []
counter = 0
for x in range(b):
    string = input()
    data = []
    if "0" in string:
        counter += 1
    else:
        counter = 0
    array.append(counter)
print(max(array))