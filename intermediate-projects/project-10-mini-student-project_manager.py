students = ['John', 'Mark', 'Anna']
grades = [85, 92, 78]

while True:
    print('==========GRADE MANAGER==========')
    print('1. View Student')
    print('2. Add Student')
    print('3. Search Student')
    print('4. Update Grade')
    print('5. Exit')
    print('=================================')

    choice = input('Enter choice:  ')
    if choice == '5':
        print('Thank you for using Grade Manager. Goodbye!')
        break

    elif choice == '1':
        print('=========STUDENT\'S=========')
        for i in range(len(students)):
            print(f'{i+1}. {students[i]} - {grades[i]}')

    elif choice == '2':
        enter_new_student = input('Enter student name:  ').title()
        enter_new_grades = int(input('Enter grade: '))
        print('---------------------------')

        students.append(enter_new_student)
        grades.append(enter_new_grades)

        print('student added successfully')
        print('----------------------------')

    elif choice == '3':
        search_student = input('Enter student name:  ').title()
        if search_student in students:
            print('Student found!')

            position = students.index(search_student)
            print(f'Grade: {grades[position]}')
        else:
            print('Student not in the list')

    elif choice == '4':
        enter_student_name = input('Enter student name: ').title()
        if enter_student_name in students:
            position = students.index(enter_student_name)
            update_student_grade = int(input('Enter grade: '))
            if 0 < update_student_grade <= 100:
                grades[position] = update_student_grade

                print('')
                print('Grade updated')
            else:
                print('Invalid Grade')
        else:
            print('Student not in the list')

    


