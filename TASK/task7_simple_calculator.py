# task7_simple_calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Handles division by zero
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x / y

def modulus(x, y):
    # Handles modulus by zero
    if y == 0:
        raise ZeroDivisionError("Cannot perform modulus with zero!")
    return x % y

def power(x, y):
    return x ** y

def get_numeric_input(prompt):
    """Helper function to get valid float input from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculator():
    """Main function for the simple calculator."""
    print("Simple Calculator")
    print("-----------------")

    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Modulus (%)")
        print("6. Power (**) ")
        print("7. Exit")

        choice = input("Enter choice(1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5', '6'):
            num1 = get_numeric_input("Enter first number: ")
            num2 = get_numeric_input("Enter second number: ")

            try:
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                elif choice == '5':
                    print(f"{num1} % {num2} = {modulus(num1, num2)}")
                elif choice == '6':
                    print(f"{num1} ** {num2} = {power(num1, num2)}")
            except ZeroDivisionError as e:
                print(f"Error: {e}")
            except Exception as e: # Catch any other unexpected errors
                print(f"An unexpected error occurred: {e}")
        else:
            print("Invalid input. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    calculator()