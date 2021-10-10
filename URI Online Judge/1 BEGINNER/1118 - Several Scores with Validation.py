result_1 = "novo calculo (1-sim 2-nao)"
while True:
    a = 0; b = 0
    while b<2:
        num = float(input())
        if num >= 0 and num <= 10:
            a += num
            b += 1
        else:
            print("nota invalida")
    result_2 = "{:.2f}".format(a/2)
    print("media =",result_2)
    while True:
        print(result_1)
        num_2 = int(input())
        if num_2 == 1 or num_2 == 2:
            break
    if num_2 == 2:
        break