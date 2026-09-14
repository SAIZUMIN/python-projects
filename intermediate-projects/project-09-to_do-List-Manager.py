tasks = ['Study Python', 'Do Homework', 'Practice Coding']

while True:
    print('============TO-DO LIST============')
    print('1. View Task')
    print('2. Add Task')
    print('3. Remove Task')
    print('4. Exit')
    print('==================================')

    choice = input('Enter choice: ')
    if choice == '4':
        print('========TASK========')
        print('Logout successfuly')
        break
    elif choice == '1':
        print('===========TASK============')
        for list in range(len(tasks)):
            print(f'{list+1}. {tasks[list]}')

        print('===========================')

    elif choice == '2':
        enter_new_task = input('Enter new task:  ')
        tasks.append(enter_new_task)

        print('Task added successfuly!')

    elif choice == '3':
        print('========TASK=========')
        for list in range(len(tasks)):
            print(f'{list+1}. {tasks[list]}')
        print('=====================')

        enter_task_remove = int(input('Enter task to remove:  '))
        if enter_task_remove <= len(tasks) and enter_task_remove > 0:
            tasks.pop(enter_task_remove - 1)

            print('Task remove successfuly!')
        else:
            print(f'Task {enter_task_remove} is not on the list')




