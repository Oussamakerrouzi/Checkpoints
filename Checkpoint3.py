def calculator(num1, num2):
    operator = input("Enter the operator (+, -, *, /): ")
    
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operator entered."

print("Welcome to the Simple Calculator!")

while True:
    try:
        print("\n--- New Calculation ---")
        first_num = float(input("Enter the first number: "))
        second_num = float(input("Enter the second number: "))
        
        result = calculator(first_num, second_num)
        
        print(f"The result is: {result}")
        
    except ValueError:
        print("Error: Invalid input. Please enter numerical values.")
    
    play_again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
    if play_again != 'yes' and play_again != 'y':
        print("Thanks for using the calculator. Goodbye!")
        break
