result = ""
number = int(input())
for x in range(number):
    string = input()
    counter = 0
    checker = "hackerrank"
    start = 0
    start2 = 0
    for x in range(len(string)):
        if start2 > 9:
            break
        elif start2 <= 9 and string[start] == checker[start2]:
            start += 1
            start2 += 1
            counter += 1
        elif start2 <= 9 and string[start] != checker[start2]:
            start += 1
    if counter == 10:
        result += "YES\n"
    else: result += "NO\n"
    print(counter)
print(result[:-1])