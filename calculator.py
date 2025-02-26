#Assignment: make a calculator using python programming

def calculator(num1, num2, operation):
    if operation == "addition":
        return num1 + num2
    elif operation == "subtraction":
        return num1 - num2    
    elif operation == "multiplication":
        return num1 * num2    
    elif operation == "division":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2    
    else:    
        return "Invalid operation"
    

#main program
def main():
    print("Welcome to the python calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Select an operation: Addition, Substraction, Multiplication, Division")
    operation = input("Enter the operation: ").strip().lower()
    result = calculator(num1, num2, operation)
    print(f"The result of {operation} is: {result}")
    
main()