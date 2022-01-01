salary = float(input())
if 0<=salary<=2000:
    print("Isento")
elif 2000 < salary <= 3000:
    tax = "{:.2f}".format((salary-2000)*0.08)
    print("R$",tax)
elif 3000 < salary <= 4500:
    tax = "{:.2f}".format(((salary-3000)*0.18)+(1000*0.08))
    print("R$",tax)
elif salary > 4500:
    tax = "{:.2f}".format(((salary-4500)*0.28)+(1500*0.18)+(1000*0.08))
    print("R$",tax)