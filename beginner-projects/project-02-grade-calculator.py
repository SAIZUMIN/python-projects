while True:
    name = input('Student name: ')
    math_grade =int(input('Math grade:  '))
    english_grade = int(input('English grade: '))
    Programming_grade = int(input('Programming grade: '))

    calculate = (math_grade + english_grade + Programming_grade )/3
    print('------------------------------------------------------')
    if math_grade < 75:
        print('failed Math grade below 75')
    elif english_grade < 75:
        print('failed Enlish grade below 75')
    elif Programming_grade < 75:
        print('failed Programming grade below 75')
    elif calculate >= 90:
        print(f'Avarage: {calculate} Execellent')
    elif calculate >= 80 and calculate <= 89:
        print(f'Avarage: {calculate} Very Good')
    elif calculate >= 75 and calculate <= 79:
        print(f'Avarage: {calculate} Passed')

    enter = input('\nEnter another Student? (Y/N): ')

    if enter.upper() != 'Y':
        print('Thank you and Goodbye')
        break
        



