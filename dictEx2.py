user = {}
while True:
    print("If you want to stop data storing enter 'end'.")
    key = input("Enter the key : ")
    if key == 'end':
        print('All Value are stored')
        break
    else:
        value = input(f"enter the value of {key} : ")
        if value > '0' and value < '9' or value == '0':
            value = int(value)
        user.update({key : value})

print(user)