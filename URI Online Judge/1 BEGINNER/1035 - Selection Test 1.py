p,q,r,s = map(int,input().split(" "))

if q>r and s>p and (r+s) > (p+q) and r>0 and s>0 and p%2 == 0:
	print( "Valores aceitos")
else:
	print("Valores nao aceitos")