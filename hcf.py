def hcf2(a, b):
    if a == 0:
        return b
    return hcf2(b % a, a)
print(hcf2(12, 15))