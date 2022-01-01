num = int(input())
if num%2 == 0:
    number = num
else:
    number = num - 1
even_list = []
for x in range(2,number+1):
    if x % 2 == 0:
        even_list.append(x)
for y in even_list:
    print(f"{y}^2 = {y**2}")