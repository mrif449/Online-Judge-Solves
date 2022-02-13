sum = 0
a,b = map(int,input().split())
array = list(map(int, input().split()))
total = int(input())
for x in array:
    sum += x
sum -= array[b]
half = sum/2
payment = total-half
if payment == 0:
    print("Bon Appetit")
else:
    print(int(payment))