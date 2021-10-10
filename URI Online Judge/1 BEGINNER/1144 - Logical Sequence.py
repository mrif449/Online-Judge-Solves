number = int(input())
for x in range(1,number+1):
    a = x
    b = x*x
    c = x*x*x
    d = b+1
    e = c+1
    print("{} {} {}".format(a,b,c))
    print("{} {} {}".format(a,d,e))