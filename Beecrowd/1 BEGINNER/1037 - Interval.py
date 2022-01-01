inp = float(input())
if inp>75 and inp<=100:
    print("Intervalo (75,100]")
elif inp>50 and inp<=75:
    print("Intervalo (50,75]")
elif inp>25 and inp<=50:
    print("Intervalo (25,50]")
elif inp>=0 and inp<=25:
    print("Intervalo [0,25]")
else:
    print("Fora de intervalo")