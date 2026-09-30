from math_utils import add, subtract, multiply, divide

while True:

    print('=== MINI UTILITY TOOLKIT ===')
    print('1. Addition')
    print('2. Substraction')
    print('3. Multiply')
    print('4. Divide')
    print('5. Exit')
    print('============================')

    choice = input('Enter choice: ')
    if choice == '1':
        try:
            enter_num1 = int(input('Enter first number: '))
            enter_num2 = int(input('Enter second number: '))
            total = add(enter_num1, enter_num2)
            print(f'Answer: {total}')
        except ValueError:
            print('Invalid number!')

    elif choice == '2':
        try:
            enter_num1 = int(input('Enter first number: '))
            enter_num2 = int(input('Enter second number: '))
            total = subtract(enter_num1, enter_num2)
            print(f'Answer: {total}')
        except ValueError:
            print('Invalid number')

    elif choice == '3':
        try:
            enter_num1 = int(input('Enter first number: '))
            enter_num2 = int(input('Enter second number: '))
            total = multiply(enter_num1, enter_num2)
            print(f'Answer: {total}')
        except ValueError:
            print('Invalid number!')

    elif choice == '4':
        try:
            enter_num1 = int(input('Enter first number: '))
            enter_num2 = int(input('Enter second number: '))
            if enter_num2 == 0:
                print('Cannot divide by 0')
            else:
                total = divide(enter_num1, enter_num2)
                print(f'Answer: {total}')
        except ValueError:
            print('Invalid number')

    elif choice == '5':
        print('Thank you for using Utility Toolkit. Goodbye!')
        break

    else:
        print('Invalid choice!')