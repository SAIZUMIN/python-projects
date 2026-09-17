student = {
    'John':{
        'Grade': 85,
        'Course': 'BSIT'
    },
    'Mark':{
        'Grade': 92,
        'Course': 'BSCS'
    },
    'Anna':{
        'Grade': 78,
        'Course': 'BSIT'
    }
}

while True:
    print('=====STUDENT RECORD MANAGER=====')
    print('1. View Student')
    print('2. Add Student')
    print('3. Search Student')
    print('4. Update Grade')
    print('5. Update Course')
    print('6. Delete Student')
    print('7. Exit')

    choice = input('Enter choice: ')
    if choice == '7':
        print('Thank You for using Student Record Manager!')
        break

    elif choice == '1':
        
        counter = 0
        print('======VIEW STUDENT======')
        for students in student:
            counter += 1
            print(f"{counter}. {students} - Course: {student[students]['Course']} - Grade: {student[students]['Grade']}")

    elif choice == '2':
        print('======ADD STUDENT======')
        student_name = input('Enter student name: ').title()
        if student_name in student or student_name == '':
            print('Student name cannot be empty or already exist!')
        else:
            student_course = input('Enter student course: ')
            if  student_course == '' :
                print('Student course can not be empty!')
            else:
                student_grade = int(input('Enter student grade: '))
                if 0 < student_grade <= 100:
                    student[student_name] = {
                        'Grade': student_grade,
                        'Course': student_course
                        }
                    print(f'Student: {student_name} succesfully added')
                else:
                    print('Grade must be greater than 0 and no more than 100!')

    elif choice == '3':
        search_student = input('Enter student name: ').title()
        if search_student in student:
                print('Student Found!')
                print(f'Name: {search_student}')
                print(f"Course: {student[search_student]['Course']}")
                print(f"Grade: {student[search_student]['Grade']}")
        else:
            print(f'No student name in the record')
    elif choice == '4':
        student_name = input('Enter student name: ').title()
        if student_name in student:
            student_new_grade = int(input('Enter new grade: '))
            if 0 < student_new_grade <= 100:
                student[student_name]['Grade'] =  student_new_grade
                print('Student grade successfully updated!')
            else:
                print('Invalid Grade!. must be > 0 and <= 100')
        else:
            print(f'Student name not in the record')

    elif choice == '5':
        student_name = input('Enter student name: ').title()
        if student_name in student:
            enter_new_course = input('Enter new Course: ')
            if enter_new_course != '':
                student[student_name]['Course'] = enter_new_course
                print('Student course successfully updated!')
            else:
                print('Student course is  empty!')
        else:
            print('Student not found!')

    elif choice == '6':
        student_name = input('Enter student name: ').title()
        if student_name in student:
            student.pop(student_name)
            print('Student successfully deleted!')
        else:
            print('Student not found!')