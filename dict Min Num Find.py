# WAP to print the minimum number in a subject for a dictionary the dictionary must be created by the user input

subject_marks = {}
while True:
    print("If you enter end the program will stop.")
    key = input("Enter the Subject name : ")
    if key == 'end':
        print('All data is saved.')
        break
    else:
        value = int(input(f"Enter the marks : "))
        subject_marks.update({key:value})

#Checking Minimum and maximum values
numbers = list(subject_marks.values())
numbers.sort()
min_num = numbers[0]
n = len(numbers)
max_num = numbers[n - 1]

# Printing Details
for sub, num in subject_marks.items():
    if num == min_num:
        print(f'The minimum subject is {sub} and number is {num}')
    elif num == max_num:
        print(f'The Maximum subject is {sub} and number is {num}')
    else:
        print('Something went Worng')