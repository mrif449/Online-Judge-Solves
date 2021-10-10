list_1 = []
limit = int(input())
num1, num2 = 0, 1
count = 0
while count < limit:
    list_1.append(num1)
    temp = num1 + num2
    num1 = num2
    num2 = temp
    count += 1
result = ""
for x in list_1:
    result += f"{x} "
print(result[:-1])