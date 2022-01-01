time = int(input())
year = time//365
time %= 365
month = time//30
time %= 30
day = time
print(year,"ano(s)")
print(month,"mes(es)")
print(day,"dia(s)")