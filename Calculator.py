
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def calculator():
    print("===== SIMPLE CALCULATOR =====")

    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("q. Quit")

        choice = input("Enter choice (1/2/3/4) or q to quit: ").strip()

        if choice.lower() == 'q':
            print("Calculator closed. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice! Please select 1, 2, 3, or 4.")
            continue

        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue

        if choice == '1':
            result = add(x, y)
        elif choice == '2':
            result = subtract(x, y)
        elif choice == '3':
            result = multiply(x, y)
        else:
            result = divide(x, y)

        print("Result:", result)


if __name__ == "__main__":
    calculator()
