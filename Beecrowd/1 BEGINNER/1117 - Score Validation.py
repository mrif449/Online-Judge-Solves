a = 0; b = 0
while True:
    if a == 2:
        break
    c = float(input())
    if c>=0 and c<=10:
        a = a+1
        b = b+c
    else:
        print("nota invalida")
result = "{:.2f}".format(b/2)
print("media =",result)