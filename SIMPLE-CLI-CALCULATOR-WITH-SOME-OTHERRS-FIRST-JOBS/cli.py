# Program make a simple calculator

print("WELCOME TO SIMPLE CLI ")
# This function adds two numbers


def add(x, y):
    return x + y

# This function subtracts two numbers


def subtract(x, y):
    return x - y

# This function multiplies two numbers


def multiply(x, y):
    return x * y

# This function divides two numbers


def divide(x, y):
    return x / y


# This function carry out modulus operation two numbers


def modulus(x, y):
    return x % y


print('-----------------------------------------')
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Division")
print("5.Modulus (REMENDER OF A NUMBER)")

print('------------------------------------------')
while True:

    # take input from the user
    print('-----------------------------------------')
    print('NOTE: your choice determine your operation.')
    print('-----------------------------------------')
    choice = input("Enter choice(1/2/3/4/5): \n")
    print('-----------------------------------------')

    # operation message to user
    if choice in ('1', '2', '3', '4', '5'):
        print('-----------------------------------------')
        if choice == '1':
            print('YOU ARE ABOUT PERFORMING ADDDITION')

        elif choice == '2':
            print('YOUR ARE ABOUT PERFORMING SUBTRACTION')

        elif choice == '3':
            print('YOUR ARE ABOUT PERFORMING MULTIPLICATION')

        elif choice == '4':
            print('YOUR ARE ABOUT PERFORMING DIVITION')

        elif choice == '5':
            print('YOUR ARE ABOUT PERFORMING MODULUS (REMENDER OF A NUMBER)')

        print('------------------------------------------')
        num1 = float(input("Enter first number: \n"))
        print('------------------------------------------')
        num2 = float(input("Enter second number: \n"))
        print('------------------------------------------')

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            print('CONGRATULATIONS YOUR ADDITION WAS CARRIED SUCCESSFULLY')

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            print('CONGRATULATIONS YOUR SUBTRACTION WAS CARRIED SUCCESSFULLY')

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            print('CONGRATULATIONS YOUR MULTIPLICATION WAS CARRIED SUCCESSFULLY')

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            print('CONGRATULATIONS YOUR DIVISION WAS CARRIED SUCCESSFULLY')

        elif choice == '5':
            print(num1, "%", num2, "=", modulus(num1, num2))
            print(
                'CONGRATULATIONS YOUR MODULUS (REMENDER OF A NUMBER) WAS CARRIED SUCCESSFULLY')

        # check if user wants another calculation
        # break the while loop if answer is no
        next_cal = input("Let's do next calculation? (yes/no): \n")
        print('------------------------------------------')

        if next_cal == "no":
            print('------------------------------------------')
            print(" THANK YOU FOR USING OUR System")
            print('------------------------------------------')
            break

    else:
        print("Invalid Input")
