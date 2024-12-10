i = 1  
while i <= 4:
    print("*" * i)
    i += 1  

print()

rows = 4
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1

print()

rows = 4
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(i, end="")
        j += 1
    print()
    i += 1