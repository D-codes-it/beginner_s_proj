#A simple python code for a creating a basic calculator
def addition (a, b):
    return a+b

def multiplication (a, b):
    return a*b

def division (a, b):
    return a/b

def subtraction (a, b):
    return a-b


print("1. Addition")
print("2. Multiplication")
print("3. Division")
print("4. Subtraction")
operation_choice = input("What operation would you like to perform?  ")


a = int(input("Enter a number:  "))
b = int(input("Enter another number:  "))

if operation_choice == "1":
    print("Addition result: ", addition(a, b))
elif operation_choice == "2":
    print("Multiplication result: ", multiplication(a, b))
elif operation_choice == "3":
    print("Division result: ", division(a, b))
elif operation_choice == "4":
    print("Subtraction result: ", subtraction(a, b))
else:
    print("Invalid choice")
