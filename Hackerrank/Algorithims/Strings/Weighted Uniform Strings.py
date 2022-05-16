result = ""
string = input().strip()
cost = set()
prev = ''
counter = 0
for i in string:
    if i != prev:
        prev = i
        counter = 0
    counter += 1
    cost.add(counter * (ord(i) - ord('a') + 1))
for _ in range(int(input())):
    if int(input()) in cost:
        result += "Yes\n"
    else:
        result += "No\n"
print(result[:-1])