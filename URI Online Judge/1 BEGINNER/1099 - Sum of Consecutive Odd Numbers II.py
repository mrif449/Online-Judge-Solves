num = int(input())
for x in range(num):
    sum = 0
    a,b = map(int,input().split())
    if a>=b:
        if b%2 == 0:
            for i in range(b,a):
                if i%2 != 0:
                    sum += i
        else:
            for j in range(b+1,a):
                if j%2 != 0:
                    sum += j
    else:
        if a%2 == 0:
            for k in range(a,b):
                if k%2 != 0:
                    sum += k
        else:
            for l in range(a+1,b):
                if l%2 != 0:
                    sum += l 
    print(sum)