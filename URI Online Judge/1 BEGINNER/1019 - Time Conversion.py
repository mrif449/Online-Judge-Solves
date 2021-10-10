time = int(input())
hour = time%60
time //= 60
minute = time%60
time //= 60
second = time%60
print(f"{second}:{minute}:{hour}")