a = input("Enter Something!: ")
if a >= 'a' and a <= 'z':
    print(a[::-1])
    print(type(a))

elif a>= '0' and a <= '9':
    num = int(a) 
    rev = 0
    while num > 0:  
        rem = num % 10
        rev = (rev * 10) + rem
        num = num // 10
    print(rev)
    print(type(rev))  

else:
    print("Something Went Wrong!")