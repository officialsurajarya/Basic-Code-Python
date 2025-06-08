l = [10,20,10,30,10,30,20,40,50,40]
targed = 10
for i in l:
    if i == targed:
        l.remove(i)
print(l)