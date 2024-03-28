def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero!"
    else:
        return num1 / num2


def main():
    print("Welcome to the Basic Calculator!")

    while True:
        print("Available operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter your choice (1-4): ")
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = None
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        if result is None:
            continue

        print("Result:", result)

        answer = input("Do you want to perform another calculation (yes/no)? ").lower()
        if answer != 'yes':
            break

    print("Thank you for using the Basic Calculator!")


if __name__ == "__main__":
    main()