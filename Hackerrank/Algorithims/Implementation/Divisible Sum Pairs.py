a,b = map(int,input().split())
array = list(map(int, input().split()))

counter = 0
for x in range(len(array)):
	for y in range(len(array)):
		if x == y:
			continue
		elif (array[x]+array[y]) % b == 0:
			counter += 1
print(int(counter/2))