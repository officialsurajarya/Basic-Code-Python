# key =  ['a', 'b', 'c']
# value = [1, 2, 3]

# dict ={}

# for k,v in zip(key, value):
#     dict.update({k:v})
# print(dict)



# s= "Suraj Arya"
# for i in s:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# print(dict)

# s = "Banana"
# freq = {}
# for i in s:
#     freq[i] = freq.get(i, 0) + 1 
# print(freq) 

# s = "Artificial Intelligence"
# s=s.lower()
# vowels = 0

# freq = {}
# for i in s:
#     if i in 'aeiou':
#         freq[i] = freq.get(i, 0) + 1
#         vowels += 1
# print(vowels)
# print(freq)

# dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# keys = list(dict.keys())
# values = list(dict.values())
# new_dict = {}
# for i in range(len(keys)):
#     new_dict[values[i]] = keys[i]
# print(new_dict)


# temp = {}
# for k in dict:
#     temp[dict[k]] = k
# print(temp)

# s = "Hello 43 % World"
# s = s.lower()
# vowels = 0
# cons = 0

# for i in s:
#     if i.isalpha(): 
#         if i in 'aeiou':
#             vowels += 1
#         else:
#             cons += 1

# print(f"Vowels: {vowels}")
# print(f"Consonants: {cons}")

# num = 12345
# sum=0
# newnum = list(str(num))
# # print(newnum)
# for i in newnum:
#     sum+= int(i)
# print(sum)

# # sum(int(i) for i in str(num))



# s = "This is a class of ml"
# splt = s.split()
# print(len(splt))


# s = "Suraj Arya 123#@"
# s = s.lower()
# new = ""
# for i in s:
#     if i.isalpha() or i.isspace():
#         new += i
# print(new)


# s1 = ' '.join(filter(str.isalpha, s))
# print(s1)

# s = "Hello In New World"
# s = s.lower()
# s = ' '.join(word[::-1] for word in s.split())
# print(s)

# find the longest word in a string
