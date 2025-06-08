# char = 'z'
# if char in 'aeiou':
#     print(char, "is Vowels")
# else:
#     print(char, 'is constant')

count=0
s = input("Enter a String: ")
for i in s:
    if i in 'aeiou':
        count+=1
print(count)