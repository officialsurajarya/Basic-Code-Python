d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 3, 'd': 4}

keyd1 = []
for key in d1:
    keyd1.append(key)
print(keyd1)

keyd2 = []
for key in d2:
    keyd2.append(key)
print(keyd2)

print(keyd1 & keyd2)
