day,date = input().split()
date = int(date)
hour,minute,second = map(int,input().split(" : "))
day,date2 = input().split()
date2 = int(date2)
hour2,minute2,second2 = map(int,input().split(" : "))

date = date2 - date
hour = hour2 - hour
minute = minute2 - minute
second = second2 - second

if second<0:
    second += 60
    minute -= 1
if minute<0:
    minute += 60
    hour -= 1
if hour<0:
    hour += 24
    date -= 1
print(date,"dia(s)")
print(hour,"hora(s)")
print(minute,"minuto(s)")
print(second,"segundo(s)")