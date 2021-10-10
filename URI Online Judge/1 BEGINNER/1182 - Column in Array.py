number = int(input())
string = input()
count = 0
for x in range(144):
    number2 = float(input())
    if x == number:
        count += number2
        number += 12
result = "{:.1f}".format(count)
result2 = "{:.1f}".format(count/12)
if string == "S":
    print(result)
else:
    print(result2)