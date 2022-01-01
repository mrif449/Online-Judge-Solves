list_1 = [0,1]
number_1 = 0
number_2 = 1
for x in range(60):
    temp = number_1 + number_2
    list_1.append(temp)
    number_1=number_2
    number_2=temp
number = int(input())
for y in range(number):
    result = int(input())
    result = str(result)
    print("Fib("+result+") =",list_1[int(result)])