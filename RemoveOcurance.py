lst=[1,2,1,2,3,4,5,1,2,3,4,1,2]

num = int(input("Enter a number"))
# for i in lst:
#     if i==num:
#         lst.remove
#         continue
# print(lst)
    
l = [x for x in lst if x !=num ]
print(l)