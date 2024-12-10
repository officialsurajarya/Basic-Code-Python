# Algorithm 
# Step 1 - Start
# Step 2 - Print the choices for the user as 1 for circle 2 for square 3 for rectangle
# Step 3 - if user choice is 1 - Then ask again the circumference of circle of area of circle
# Step 4 - for circumference - 2*pi*r and for area of circle - pi*r^2, then print the corresponding values.
# Step 5 - if user choice 2 - then ask again the area of square or parameter of square
# Step 6 - for area side^2
# Step 7 - for perimeter 4*side
# Step 8 - if user choice 3 - then ask again area of rectangle or parameter of rectangle
# Step 9 - for area of rectangle length*breadth
# Step 10 - for parameter of rectangle 2*(l+b)
# Step n - if user chooses the wrong choice throw a message "Something went wrong"
# Step n + 1 - stop

print("Choose the correct option.\n1. Circle\n2. Square\n3. Rectangle\n")
choice = int(input())

if choice == 1:
    print("1. Area of circle\n2. Circumference of circle\n")
    c_choice = int(input("Enter your choice: "))
    pi = 3.14
    r = int(input("Enter the value of radius: "))
    if c_choice == 1:   
        a = pi * (r ** 2)
        print(f"The area of the circle is: {a}")
    elif c_choice == 2:
        c = 2 * pi * r
        print(f"The circumference of the circle is: {c}")
    else:
        print("Something went wrong.")
elif choice == 2:
    side = int(input("Enter the side length of the square: "))
    print("1. Area of square\n2. Perimeter of square\n")
    s_choice = int(input("Enter your choice: "))
    if s_choice == 1:
        a = side ** 2
        print(f"The area of the square is: {a}")
    elif s_choice == 2:
        p = 4 * side
        print(f"The perimeter of the square is: {p}")
    else:
        print("Something went wrong.")
elif choice == 3:
    length = int(input("Enter the length of the rectangle: "))
    breadth = int(input("Enter the breadth of the rectangle: "))
    print("1. Area of rectangle\n2. Perimeter of rectangle\n")
    r_choice = int(input("Enter your choice: "))
    if r_choice == 1:
        a = length * breadth
        print(f"The area of the rectangle is: {a}")
    elif r_choice == 2:
        p = 2 * (length + breadth)
        print(f"The perimeter of the rectangle is: {p}")
    else:
        print("Something went wrong.")
else:
    print("Something went wrong.")