grade_a = 15
grade_b = 12
grade_c = 10
grade_d = 7
grade_e = 4
salary = float(input())
if 0<=salary<=400.00:
    bonus = salary+(salary/100*grade_a)
    result = "{:.2f}".format(bonus)
    extra = float(result) - float(salary)
    result_2 = "{:.2f}".format(extra)
    print("Novo salario:",result)
    print("Reajuste ganho:",result_2)
    print("Em percentual:",grade_a,"%")
elif 400.01<=salary<=800.00:
    bonus = salary+(salary/100*grade_b)
    result = "{:.2f}".format(bonus)
    extra = float(result) - salary
    result_2 = "{:.2f}".format(extra)
    print("Novo salario:",result)
    print("Reajuste ganho:",result_2)
    print("Em percentual:",grade_b,"%")
elif 800.01<=salary<=1200.00:
    bonus = salary+(salary/100*grade_c)
    result = "{:.2f}".format(bonus)
    extra = float(result) - salary
    result_2 = "{:.2f}".format(extra)
    print("Novo salario:",result)
    print("Reajuste ganho:",result_2)
    print("Em percentual:",grade_c,"%")
elif 1200.01<=salary<=2000.00:
    bonus = salary+(salary/100*grade_d)
    result = "{:.2f}".format(bonus)
    extra = float(result) - salary
    result_2 = "{:.2f}".format(extra)
    print("Novo salario:",result)
    print("Reajuste ganho:",result_2)
    print("Em percentual:",grade_d,"%")
elif salary>2000.00:
    bonus = salary+(salary/100*grade_e)
    result = "{:.2f}".format(bonus)
    extra = float(result) - salary
    result_2 = "{:.2f}".format(extra)
    print("Novo salario:",result)
    print("Reajuste ganho:",result_2)
    print("Em percentual:",grade_e,"%")