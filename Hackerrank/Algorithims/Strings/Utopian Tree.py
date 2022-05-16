result = ""
count = int(input())
for x in range(count):
    number = int(input())
    sum = 0
    for x in range(1,number+2):
        if x%2 == 0:
            sum*= 2
        else:
            sum += 1
    result += str(sum)+"\n"
print(result[:-1])