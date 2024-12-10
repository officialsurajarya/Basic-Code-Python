#Write a program to check that inputed number is positive negitive or zero
num = int(input("Enter a Number: "))
if 0<num:
    print(num,"is Positive")
elif 0>num:
    print(num,"is Negative")
else:
    print(num,"is Zero")