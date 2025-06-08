a = 5                               #data type is implicitly set to integer
print(a, " is of type", type(a))

a = 2.5                            #data type is changed to float
print(a, " is of type", type(a))


a = 1 + 2j                          #data type is changed to complex number
print(a," is of type", type(a))
print(isinstance(1+2j, complex))



a = True                          #a is a boolean type
print(type(a))