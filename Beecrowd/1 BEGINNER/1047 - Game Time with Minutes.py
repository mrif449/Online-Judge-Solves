h1,m1,h2,m2=list(map(int,input().split(" ")))
differnce = ((h2*60)+m2)-((h1*60)+m1)
if differnce <= 0:
    differnce += 24*60
hour = differnce//60
minute = differnce%60
print("O JOGO DUROU",hour,"HORA(S) E",minute,"MINUTO(S)")