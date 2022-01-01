list1 = []
for x in range(5):
    num = int(input())
    if num%2 == 0:
        list1.append(num)
print(len(list1),"valores pares")