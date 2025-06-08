lst = [6,5,7,3,2,8,1]
even=[]
odd=[]

for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even+odd)