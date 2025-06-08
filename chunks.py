# split a list in size of chunks n
lst= [10, 20, 10,4, 45, 99, 120]
n=2
print([lst[i:i+n] for i in range(0, len(lst), n)])

