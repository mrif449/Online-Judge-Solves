array = []
string = input()
for x in string:
    if x != " " and x.lower() not in array:
        array.append(x.lower())
if len(array) == 26:
    print("pangram")
else:
    print("not pangram")