# WAP to convert to list into dictionary 

li1 = ['key1'+'key2'+'key3']
li2 = ['value1'+'value2'+'value3']

dict = {}

for i in range(len(li1)):
    dict.update({li1[i] : li2[i]})

print(dict)