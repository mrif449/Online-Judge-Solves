import math
counter = 0
number = int(input())
for x in range(number):
	a,b = map(int,input().split())

	temp1 = int(math.sqrt(b))
	temp2 = int(math.sqrt(a-1))
	print(temp1-temp2)