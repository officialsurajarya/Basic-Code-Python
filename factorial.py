n = int(input("Enter a Number: "))
num = n
f = 1
while(n!=0):
    f=f*n
    n-=1
print("Factorial of",num,"is: ",f)