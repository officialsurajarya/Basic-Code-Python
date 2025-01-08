num1 = int(input("Enter 1st no.: "))
num2 = int(input("Enter 2nd no.: "))
num3 = int(input("Enter 3rd no.: "))

if (num1>num2 and num1>num3):
    print("First Number is Greatest")
elif (num2>num3):
    print("Second Number is Greatest")
else:
    print("Third Number is Greatest")