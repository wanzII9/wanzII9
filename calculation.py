def calculator():
    print("Welcome to the simple calculator!")
    print("You can use the following operators: + for addition, - for subtraction, * for multiplication, / for division.\n")

    # Get first number
    try:
        num1 = float(input("Please enter the first number: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    # Get operator
    op = input("Enter an operator (+, -, *, /): ")

    # Get second number
    try:
        num2 = float(input("Please enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    # Perform calculation
    if op == '+':
        result = num1 + num2
        operation = "addition"
    elif op == '-':
        result = num1 - num2
        operation = "subtraction"
    elif op == '*':
        result = num1 * num2
        operation = "multiplication"
    elif op == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
        operation = "division"
    else:
        print("Invalid operator. Please use one of +, -, *, or /.")
        return

    # Show result
    print(f"\nThe result of the {operation} between {num1} and {num2} is: {result}")

calculator()
