fine = 0
d1, m1, y1 = map(int,input().split())
d2, m2, y2 = map(int,input().split())
if y1-y2 >= 1:
    fine = 10000
elif y1-y2 < 1:
    if m1-m2 < 1 and d1-d2 > 0:
        fine = (d1-d2)*15
    elif m1-m2 >= 1:
        fine = (m1-m2)*500
if y1-y2 < 0 or (y1==y2 and m1-m2<0):
    fine = 0
print(fine)