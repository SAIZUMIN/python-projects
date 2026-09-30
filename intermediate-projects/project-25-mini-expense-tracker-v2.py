expenses = {
    'Food': 150,
    'Transportation': 50,
    'School': 200
}
def view_expenses(expenses):
    count = 0
    if not expenses:
        print('No expense found!')
    else:
        for expense in expenses:
            count += 1
            print(f"{count}. {expense} - {expenses[expense]}")

def add_expense(expenses):
    enter_name = input('Enter name: ').title()
    if enter_name in expenses:
        print('expense already exist!')
    elif enter_name == '':
        print('Enter a valid name')
    else:
        while True:
            try:
                enter_amount = int(input('Enter amount: '))
                if enter_amount <= 0:
                    raise ValueError
                else:
                    expenses[enter_name] = enter_amount
                    print('Expense added successfully!')
                    break
            except ValueError:
                print(f'Invalid amount!')

def search_expense(expenses):
    enter_name = input('Enter name: ').title()
    if enter_name in expenses:
        print(f'{enter_name} - {expenses[enter_name]}')
    else:
        print('Name not found!')

def delete_expense(expenses):
    enter_name = input('Enter name: ').title()
    if enter_name in expenses:
        expenses.pop(enter_name)
        print('Name deleted successfully!')
    else:
        print('Name not found!')

def show_total(expenses):
    total = 0
    for expense in expenses:
        total += expenses[expense]
    print(f'Total Expenses: {total}')
while True:
    print('===== EXPENSE TRACKER V2 =====')
    print('1. View Expenses')
    print('2. Add Expenses')
    print('3. Search Expense')
    print('4. Delete Expense')
    print('5. Show Total')
    print('6. Exit')
    print('==============================')

    choice = input('Enter choice: ')
    if choice == '1':
        view_expenses(expenses)

    elif choice == '2':
        add_expense(expenses)

    elif choice == '3':
        search_expense(expenses)

    elif choice == '4':
        delete_expense(expenses)

    elif choice == '5':
        show_total(expenses)

    elif choice == '6':
        print('Thank you for using Expense Tracker. Goodbye!')
        break

    else:
        print('Invalid choice!')        
