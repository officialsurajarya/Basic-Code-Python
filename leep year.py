# WAP to check entered year is leep year or not
year = int(input("enter a year: "))
if year % 4 == 0:
    print(year," is a leap Year")
else:
    print(year, "is not a leap year")