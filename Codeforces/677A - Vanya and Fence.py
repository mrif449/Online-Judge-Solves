a,b =  map(int, input().split())
numbers = list(map(int, input().split()))
counter = 0
for x in range(a):
	if numbers[x] > b:
		counter += 2
	else: counter += 1

print(counter)
