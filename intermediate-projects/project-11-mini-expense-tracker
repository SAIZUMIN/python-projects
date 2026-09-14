expenses = ['Food', 'Transportation', 'School']
amounts = [150, 50 ,200]
total_expense = 0

while True:
    print('======EXPENSE TRACKER======')
    print('1. View expenses')
    print('2. Add expense')
    print('3. Search expense')
    print('4. Delete expense')
    print('5. Show total')
    print('6. Exit')

    choice = input('Enter choice: ')
    if choice == '6':
        print('Thank you for using Expense Tracker. Goodbye!')
        break

    elif choice == '1':
        print('=======EXPENSES=======')
        for i in range(len(expenses)):
            print(f'{i+1}. {expenses[i]} - {amounts[i]}')
        print('======================')

    elif choice == '2':
        expense_name = input('Enter expense name: ').title()
        expense_amount = int(input('Enter expense amount: '))
        if expense_amount > 0:
            expenses.append(expense_name)
            amounts.append(expense_amount)
            print('Expense added successfully!')
        else:
            print('negative expense amount')

    elif choice == '3':
        expense_name = input('Enter expense name: ').title()
        if expense_name in expenses:
            print('Expense found!')
            position = expenses.index(expense_name)
            print(f'Amount: {amounts[position]}')
        else:
            print('Expense not found!')

    elif choice == '4':
        expense_name = input('Enter expense name to delete: ').title()
        if expense_name in expenses:

            position = expenses.index(expense_name)
            expenses.pop(position)
            amounts.pop(position)

            print('Expense deleted!')
        else:
            print('expense not found!')
                   
    elif choice == '5':
        for i in range(len(amounts)):
            total_expense += amounts[i]

        print(f'Total expenses: {total_expense}')
        total_expense = 0

    else:
        print('Invalid')


