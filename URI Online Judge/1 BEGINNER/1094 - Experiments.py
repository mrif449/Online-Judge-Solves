c = []
r = []
s = []
num = int(input())
for x in range(num):
    number = input().split(" ")
    if number[1] == "C":
        c.append(int(number[0]))
    if number[1] == "R":
        r.append(int(number[0]))
    if number[1] == "S":
        s.append(int(number[0]))

sum_c = 0
sum_r = 0
sum_s = 0
for p in c:
    sum_c += p
for q in r:
    sum_r += q
for r in s:
    sum_s += r
sum = sum_c + sum_r + sum_s
percentage_c = "{:.2f}".format((sum_c*100)/sum)
percentage_r = "{:.2f}".format((sum_r*100)/sum)
percentage_s = "{:.2f}".format((sum_s*100)/sum)
print("Total:",sum,"cobaias")
print("Total de coelhos:",sum_c)
print("Total de ratos:",sum_r)
print("Total de sapos:",sum_s)
print("Percentual de coelhos:",percentage_c,"%")
print("Percentual de ratos:",percentage_r,"%")
print("Percentual de sapos:",percentage_s,"%")