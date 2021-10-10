start,end=list(map(int,input().split()))
if(start < end):
    duration = start-end
else:
    duration = end + 24-start
print(f"O JOGO DUROU {abs(duration)} HORA(S)")