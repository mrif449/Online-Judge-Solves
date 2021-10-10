result_1 = "Novo grenal (1-sim 2-nao)"
result_2 = "Inter venceu mais"
result_3 = "Gremio venceu mais"
result_4 = "Nao houve vencedor"

a,b,c,d,e,f = 0,0,0,0,0,0

while True:
    x,y = list(map(int,input().split()))
    if x>y:
        a += 1
    if x<y:
        b += 1
    if x==y:
        c += 1
    d+=x; e+=y; f+=1
    print(result_1)
    number = int(input())
    if number == 1:
        continue
    elif number == 2:
        break
print(f,"grenais")
print("Inter:"+str(a))
print("Gremio:"+str(b))
print("Empates:"+str(c))
if a>b:
    print(result_2)
elif b>a:
    print(result_3)
else:
    print(result_4)