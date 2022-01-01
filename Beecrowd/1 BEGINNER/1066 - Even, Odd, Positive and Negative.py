even =  []
odd = []
positive = []
negative = []
for x in range(5):
    num = int(input())
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
print(len(even),"valor(es) par(es)")
print(len(odd),"valor(es) impar(es)")
print(len(positive),"valor(es) positivo(s)")
print(len(negative),"valor(es) negativo(s)")