n,k =  map(int, input().split())
 
for x in range(k):
	if str(n)[-1] == "0":
		n = int(str(n)[:-1])
	else:
		n-=1
if n > 1:
	print(n)
else: print(1)
