a,b=list(map(int,input().split()))
if(a == 1):
    price  = (float) (4.00 * b)
elif(a == 2):
    price  = (float) (4.50 * b)
elif(a == 3):
    price  = (float) (5.00 * b)
elif (a == 4):
    price  = (float) (2.00 * b);
elif (a == 5):
    price  = (float) (1.50 * b)
print(f"Total: R$ {price:.2f}")