# # Sum And Product OF List
# listSum = [2,4,5,6,4,1,2]
# sum=0
# product=1
# for i in listSum:
#     sum+=i
#     product*=i
# print("sum of all no. :", sum)
# print("product of all no. :", product)


# total=0
# listSumStr = ["2","4","5","6","4","1","2"]
# num = list(map(int,listSumStr))
# for i in num:
#     total+=i
# print(total) 

# Sum of even number
# total = 0
# for i in range(14):
#     if i%2==0:
#         total+=i
# print(total)

howMuch=0
myList = [1,2,1,2,3,1,3,3,2,1]
num = int(input("Enter Number"))
for element in myList:
    if element==num:
        howMuch+=1
print(num,"is", howMuch,"time in List")
