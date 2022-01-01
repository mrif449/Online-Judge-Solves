product1 = input().split(" ")
product2 = input().split(" ")
p1 = float(product1[1])
p2 = float(product1[2])
p3 = float(product2[1])
p4 = float(product2[2])
result = p1*p2+p3*p4
result = "{:.2f}".format(result)
print("VALOR A PAGAR: R$",result)