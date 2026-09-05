def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "undefined (cannot divide by zero)"
    return x / y


def power(x, y):
    return x ** y


def recur_factorial(number):
    if number < 0:
        return "undefined (factorial needs a non-negative number)"
    factorial = 1
    for value in range(2, number + 1):
        factorial *= value
    return factorial


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def show_results(first_number, second_number):
    print("\nResults")
    print("Sum:", add(first_number, second_number))
    print("Difference:", subtract(first_number, second_number))
    print("Product:", multiply(first_number, second_number))
    print("Quotient:", divide(first_number, second_number))
    print("Power:", power(first_number, second_number))
    print("Factorial of", first_number, ":", recur_factorial(first_number))
    print("Factorial of", second_number, ":", recur_factorial(second_number))


def chaos():
    print("\nCHAOS MODE")
    big_number1 = get_integer("Enter a big number: ")
    big_number2 = get_integer("Enter another big number: ")
    show_results(big_number1, big_number2)


number1 = get_integer("Enter number 1: ")
number2 = get_integer("Enter number 2: ")
show_results(number1, number2)

chaos()