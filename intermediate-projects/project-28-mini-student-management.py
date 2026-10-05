class Student:
    def __init__ (self, name: str, age: int, course: str, grade: int ):
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade

    def show_student(self):
        print('===== STUDENT =====')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Course: {self.course}')
        print(f'Grade: {self.grade}')
        print('===================')

    def update_grade(self, new_grade):
        self.grade = new_grade

    def show_status(self):
        if self.grade >= 75:
            print('Passed')
        else:
            print('Failed!')

student1 = Student('Jodell', 21, 'BSIT', 95)
student2 = Student('Dale', 21, 'BSIT', 96)
student3 = Student('Jade', 21, 'BSIT', 97)

students = [student1, student2, student3]




while True:
    print('===== STUDENT MANAGEMENT =====')
    print('1. View Students')
    print('2. Search Student')
    print('3. Update Grade')
    print('4. Show Student Status')
    print('5. Exit')
    print('==============================')

    choice = input('Enter choice: ')
    if choice == '1':
        for student in students:
            student.show_student()

    elif choice == '2':
        name = input('Enter student name: ').title()
        found = False
        for student in students:
            if name == student.name:
                found = True
                print('Student Found!')
                print(f'Student: {name}')
                print(f'Age: {student.age}')
                print(f'Course: {student.course}')
                print(f'Grade: {student.grade}')

        if not found:
            print('Student not found')

    elif choice == '3':
        name = input('Enter student name: ').title()
        found = False
        for student in students:
            if name == student.name:
                found = True
                try: 
                    new_grade = int(input('Enter new grade: '))
                    if new_grade <= 0 or new_grade > 100:
                        print('Invalid Grade')
                    else:
                        student.update_grade(new_grade)
                        print('Grade successfully updated!')
                except ValueError:
                    print('Invalid Grade!')
    
        if not found:
            print('Name not found!')

    elif choice == '4':
        name = input('Enter student name: ').title()
        found = False
        for student in students:
            if name == student.name:
                found = True
                student.show_status()
        if not found:
            print('Student not found!')

    elif choice == '5':
        print('Thank you for using Student Management. Goodbye!')
        break

    else:
        print("Invalid Choice!")