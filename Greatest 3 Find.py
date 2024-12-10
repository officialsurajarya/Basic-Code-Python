#WAP to check the greatest number among 3 numbers 

#Algorithm
# Step 1 - Start
# Step 2 - take 3 input from user 
# Step 3 - compare a with b and a with c 
# Step 4 - if a greatest then print a is greatest
# Step 5 - compare b with c 
# Step 6 - if b is greatest then print b is greatest``
# Step 7 - else c is greatest
# Step 8 - stop

a = float(input("Enter Number A: "))
b = float(input("Enter Number B: "))
c = float(input("Enter Number C: "))
if (a >= b and a >= c):
    print("A is greatest")
elif(b >= a and b >= c ):
    print("B is Greatest")
elif(c >= a and c >= b):
    print("C is Greatest")
else:
    print("Somethin went worng")