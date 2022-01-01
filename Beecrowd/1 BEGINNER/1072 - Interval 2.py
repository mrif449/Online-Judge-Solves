in1 = []
out = [] 
num = int(input())
for x in range(num):
    number = int(input())
    if 10<=number<=20:
        in1.append(number)
    else:
        out.append(number)
print(len(in1),"in")
print(len(out),"out")