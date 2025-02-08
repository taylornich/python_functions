# Question 1 task 1


def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0: 
        return "Error: Division by zero is not allowed."
    return a / b


# Question 1 task 2
desired_operation = input("What operation would you like to use? (addition, subtraction, multiplication, division): ").lower()

if desired_operation not in ["addition", "subtraction", "multiplication", "division"]:
    print("Invalid operation. Please choose a valid operation.")
else:
    a = float(input("Enter the first number you would like to use: "))
    b = float(input("Enter the second number you would like to use: "))

    if desired_operation == "addition":
        result = addition(a, b)
    elif desired_operation == "subtraction":
        result = subtraction(a, b)
    elif desired_operation == "multiplication":
        result = multiplication(a, b)
    elif desired_operation == "division":
        result = division(a, b)

    # Question 1 task 3
    if isinstance(result, str):
        print(result)
    else:
        print(f"Result: {result}")



