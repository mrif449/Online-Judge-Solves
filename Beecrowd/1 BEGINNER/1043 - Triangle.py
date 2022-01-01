a,b,c = map(float,input().split())
if (a+b) > c and (b+c) > a and (a+c) > b:
    print("Perimetro =",a+b+c)
else:
    print("Area =",(a+b)/2*c)