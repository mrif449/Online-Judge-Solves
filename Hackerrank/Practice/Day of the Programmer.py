leap = "12.09."
not_leap = "13.09."
year = int(input())
if year == 2400:
    print(f"{leap}{year}")
elif year == 1918:
    print("26.09.1918")
elif  year > 2000 and (year%100 == 0):
        print(f"{not_leap}{year}")
elif  year <= 2000 and (year%100 == 0):
        print(f"{leap}{year}")
elif (year%100 != 0) and (year%4 == 0):
    print(f"{leap}{year}")

else:
    print(f"{not_leap}{year}")
