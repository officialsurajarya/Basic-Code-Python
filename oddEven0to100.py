# a = 0
# while a <= 100:
#     if a % 2 == 0:
#         print (a,"Even Number")
#     else:
#         print (a,"odd number") 
#     a += 1

a = 0
even = []
odd = []
while a <= 100:
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a) 
    a += 1

print("Odd Number's are: ",odd)
print("Even Number's are: ",even)    