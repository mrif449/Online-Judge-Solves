username = input()
array = []
for x in username:
    if x not in array:
        array.append(x)
if len(array)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")