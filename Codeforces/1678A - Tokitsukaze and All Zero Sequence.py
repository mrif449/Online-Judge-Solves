result = ""
number = int(input())
for x in range(number):
    limit = int(input())
    string = list(map(int, input().split()))
    zero = 0
    array = []
    for x in string:
        if x == 0:
            zero += 1
    
    for y in string:
        if y not in array:
            array.append(y)
    if zero >= 1:
        ans = limit - zero
    elif len(string) != len(array):
        ans = limit
    else:
        ans = limit + 1
    result += str(ans)+"\n"
print(result[:-1])