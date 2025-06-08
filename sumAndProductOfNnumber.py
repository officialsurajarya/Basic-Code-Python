n = int(input("Enter the number: "))
sum=0
product = 1
for i in range(1, n+1):
    sum+=i
    product*=i
print(sum)
print(product)
