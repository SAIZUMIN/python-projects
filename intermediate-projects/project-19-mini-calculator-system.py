def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    print('===== MINI CALCULATOR =====')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exit')
    print('===========================')

    enter_choice = int(input('Enter choice: '))

    if enter_choice == 5:
        print('Thank you for using mini calculator!')
        break
    elif 0 < enter_choice <= 4:
        first_number = int(input('Enter first number: '))
        second_number = int(input('Enter second number: '))

        if enter_choice == 1:
            result = add(first_number, second_number)
            print(f'Result: {result:.2f}')

        elif enter_choice == 2:
            result = subtract(first_number, second_number)
            print(f'Result: {result:.2f}')

        elif enter_choice == 3:
            result = multiply(first_number, second_number)
            print(f'Result: {result:.2f}')

        elif enter_choice == 4:
            if second_number == 0:
                print('Invalid Number!')
            else:
                result = divide(first_number, second_number)
                print(f'Result: {result:.2f}')
        else:
            print('Invalid choice!')
    else:
        print('Invalid!')
    
    
