# Define our function
def calculate():
    operation = input('''
Type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

    if operation == '+':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)

    elif operation == '-':
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)

    elif operation == '*':
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)

    elif operation == '/':
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)

    else:
        print('Try again')

# Call calculate() outside of the function
calculate()