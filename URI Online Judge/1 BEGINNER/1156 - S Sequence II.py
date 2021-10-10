sum = 0
number = 3
multiple = 2
while number<=39:
    while multiple<524288:
        result = number/multiple
        sum += result
        multiple *= 2
    number += 2
print("{:.2f}".format(sum+1))