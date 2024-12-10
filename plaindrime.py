num = int(input("Enter Something!: "))
temp = num
rev = 0
while num > 0:  
    rem = num % 10
    rev = (rev * 10) + rem
    num = num // 10
if rev == temp:
    print(temp,"is Palindrome Number") 
else:
    print(temp,"is Not a Palindrome")