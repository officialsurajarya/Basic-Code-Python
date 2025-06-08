lst = [5,6,4,4,3,4,5,3,6,3,5,5,3,6,4,5,3,4,5,6,3,4,5,6,3,4,5,6]
chunk_size = 2
print(lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size))
