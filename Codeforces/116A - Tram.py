count = int(input())
max = 0
passenger = 0
for x in range(count):
	a,b =  map(int, input().split())
	passenger -= a
	passenger += b
	if max<passenger:
		max = passenger
print(max)
