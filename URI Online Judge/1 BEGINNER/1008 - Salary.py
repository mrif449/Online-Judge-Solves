NUMBER = int(input())
working_hour = int(input())
rate = float(input())
salary = working_hour*rate
format_float = "{:.2f}".format(salary)
print("NUMBER =",NUMBER)
print("SALARY = U$",format_float)