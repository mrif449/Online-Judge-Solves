num = int(input())
for x in range(num):
    sum = 0
    a,b,c = map(float,input().split())
    average = (2*a+3*b+5*c)/(2+3+5)
    result = "{:.1f}".format(average)
    print(result)