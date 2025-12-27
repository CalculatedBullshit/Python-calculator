#this is my first attempt at creating a calculator in python

print("This is a simple 4 operations calculator that will accept the user input and do the operation.")
b=input("what operation is to be done out of +, -, x, and ∕ (answer with these symbols only)")
print(b)

c=float(input("Enter the first number:"))
d=float(input("Enter the second number:"))

if b=="+":
    print("The addition of these two numbers is ", c+d)

elif b=="-":
    print("The subtraction of these two numeers is ", c-d)

elif b=="x":
    print("The multiplication of these two numbers is ", c*d)

elif b=="/":
    print("The division of the these two numbers is ", c/d)

else:
    print("The operator is invalid. Please try again.")

