# question 1 task 1

import pdb

def addition(a, b):
    return a+b
sum = addition(1,1)
print(sum)

def subtraction(a,b):
    return a - b
difference = subtraction(1,1)
print(difference)

def multiplication(a, b):
    return a * b
product = multiplication(1, 1)
print(product)

def division(a, b):
    return a / b
quotient = division(1, 1)
print(quotient)


# question 1 task 2

desired_operation = input("What operation would you like to use?")
a = float(input("Enter the first number you would like to use: "))
b = float(input("Enter the second number you would like to use: "))

if desired_operation == "addition":
    result = a + b

elif desired_operation == "subtraction":
    result = a - b

elif desired_operation == "multiplication":
    result = a * b

# question 1 task 2 and 3
elif desired_operation == "division":
    if a or b == 0:
        print("Zero division invalid")
    else:
        result = a / b

print(f"Result: {result}")



