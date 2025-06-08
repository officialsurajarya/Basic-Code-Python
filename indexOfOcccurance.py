s = [1, 2, 3, 2, 4, 2]
n = 2
indx = []
for i,val in enumerate(s):
    if val == n:
        indx.append(i)
print(indx)

# print([i for i,x in enumerate(s) if x==n])

