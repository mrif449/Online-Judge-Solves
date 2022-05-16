d1 = 0
d2 = 0
d21 = []
number = int(input())
for x in range(number):
    array = list(map(int, input().split()))
    d1 += array[x]
    d2 += array[number-(x+1)]
result = (d1-d2)
if result < 0:
    result *= -1
print(result)