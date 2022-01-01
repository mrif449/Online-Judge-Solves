a,b,c = map(float,input().split())
list_1 = [a,b,c]
list_1.sort()
list_1.reverse()
if list_1[0]>=list_1[1]+list_1[2]:
    print("NAO FORMA TRIANGULO")
elif list_1[0]**2 == list_1[1]**2 + list_1[2]**2:
    print("TRIANGULO RETANGULO")
elif list_1[0]**2 > list_1[1]**2 + list_1[2]**2:
    print("TRIANGULO OBTUSANGULO")
elif list_1[0]**2 < list_1[1]**2 + list_1[2]**2:
    print("TRIANGULO ACUTANGULO")
if list_1[0] == list_1[1] == list_1[2]:
    print("TRIANGULO EQUILATERO")
elif list_1[0] == list_1[1] or list_1[1] == list_1[2]:
    print("TRIANGULO ISOSCELES")
