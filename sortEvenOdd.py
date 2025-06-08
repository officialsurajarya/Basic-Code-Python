lst = [2,7,4,6,8,1,3,5]
even = []
odd = []
for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
finalLst = even + odd
print(finalLst)