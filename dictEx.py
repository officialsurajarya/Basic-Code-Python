# name = input("Enter name")
# salary = input("Enter salary")
# email = input("Enter email")

name = 'Suraj Arya'
salary = '999k'
email = 'officialsurajary@gmail.com'

user = {
    'name' : name,
    'salary' : salary,
    'email' : email
}


print(user.keys())
userInput = input("What you want to print : ")

if userInput == 'name':
    print(user['name'])
elif userInput == 'salary':
    print(user['salary'])
elif userInput == 'name':
    print(user['email'])
else:
    print("Something went worng")
