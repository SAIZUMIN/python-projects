employee = {
    'John':{
        'Salary': 25000,
        'Department': 'IT'
    },
    'Mark':{
        'Salary': 30000,
        'Department': 'HR'
    },
    'Anna':{
        'Salary': 28000,
        'Department': 'IT'
    }
}

while True:
    print('=====EMPLOYEE MANAGER=====')
    print('1. View Employee')
    print('2. Add Employee')
    print('3. Search Employee')
    print('4. Update Salary')
    print('5. Update Department')
    print('6. Delete Employee')
    print('7. Show Total Salary')
    print('8. Exit')
    print('==========================')

    choice = input('Enter choice: ')
    if  choice == '8':
        print('Thank you for using Employee Manager!')
        break

    elif choice == '1':
        count = 0
        for employees in employee:
            count += 1
            print(f"{count}. {employees} - {employee[employees]['Salary']} - {employee[employees]['Department']}")

    elif choice == '2':
        employee_name = input('Enter employee name: ').title()
        if employee_name in employee or employee_name == '':
            print('Employee name empty or  already exist!')
        else:
            employee_salary = int(input('Enter employee salary: '))
            if employee_salary <= 0:
                print('Invalid Salary!')
            else:
                employee_department = input('Enter employee Department: ').title()
                if employee_department == '':
                    print('Invalid. Empty Department!')  
                else:
                    employee[employee_name] = {
                        'Salary': employee_salary,
                        'Department': employee_department
                    } 
                    print('Employee added successfully!')

    elif choice == '3':
        search_employee = input('Enter employee name: ').title()
        if search_employee in employee:
            print('Employee Found: ')
            print(f"{search_employee} - {employee[search_employee]['Salary']} - {employee[search_employee]['Department']}")
        else:
            print('Employee not found!')

    elif choice == '4':
        employee_name = input('Enter employee name: ').title()
        if employee_name in employee:
            update_salary = int(input('Enter new salary: '))
            if update_salary <= 0:
                print('Invalid Salary!')
            else:
                print('Salart updated!')
                employee[employee_name]['Salary'] = update_salary
        else:
            print('Employee not found!')

    elif choice == '5':
        employee_name = input('Enter employee name: ').title()
        if employee_name in employee:
            update_department = input('Enter new department: ').title()
            if update_department == '':
                print('Invalid. Empty Department!')
            else:
                employee[employee_name]['Department'] = update_department
                print('Department updated!')
        else:
            print('Employee not found!')

    elif choice == '6':
        employee_name = input('Enter employee name: ').title()
        if employee_name in employee:
                employee.pop(employee_name)
                print('Deleted successfuly!')
        else:
            print('Employee not found!')

    elif choice == '7':
        total = 0
        for employees in employee:
            total += employee[employees]['Salary']
        print(f'Total salary: {total}')
