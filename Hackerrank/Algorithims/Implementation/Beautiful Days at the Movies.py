a,b,c = map(int,input().split())
array = []
array2 = []
for x in range(a,b+1):
	array.append(x)
for y in range(len(array)):
	temp1 = str(array[y])
	temp2 = temp1[::-1]
	temp3 = int(temp2)
	array2.append(temp3)
counter = 0
for z in range(len(array)):
	temp = (array[z]-array2[z])/c
	if temp//1 == temp:
		counter += 1
print(counter)