f = open("a.txt", "w")
f.write("Good to see you")
f.close()

# Open and read the file after overwriting:
f = open("a.txt", "r")
print(f.read())