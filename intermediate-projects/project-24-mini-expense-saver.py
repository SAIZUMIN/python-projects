expenses = []


def load_expense():
    file = open('expenses.txt', 'r')
    content = file.read().splitlines()
    for expense in content:
        parts = expense.split(',')
        name = parts[0]
        amount = int(parts[1])
        expenses.append([name, amount])
    file.close()

    return expenses

def view_expenses(expenses):
    if len(expenses) == 0:
        print('EMPTY!!!')

    else:
        count = 0
        for expense in expenses:
            count += 1
            print(f'{count}. {expense[0]} - {expense[1]}')

def add_expense(expenses):
    name = input('Enter expense name: ').title()
    if name == '':
        print('Invalid name!')
    else:
        enter_amount = int(input('Enter amount: '))
        if enter_amount > 0:
            expenses.append([name, enter_amount])
        else:
            print('Invalid Amount!')

def search_expense(expenses):
    enter_name = input('Enter name: ').title()
    found = False
    for expense in expenses:
        if enter_name == expense[0]:
            print(f'{enter_name} - {expense[1]}')
            found = True
    if not found:
        print('No matching expense!')

def delete_expense(expenses):
    enter_number = int(input('Enter expense number: '))
    if enter_number >= 1 and enter_number <= len(expenses):
        expenses.pop(enter_number-1)
        print('Expense deleted!')
    else:
        print('Invalid Number!')

def show_total(expenses):
    total = 0
    for expense in expenses:
        total += expense[1]
    print(f'Total Expense: {total}')
    
def save_expenses(expenses):
    file = open('expenses.txt', 'w')
    for expense in expenses:
        file.write(f'{expense[0]},{expense[1]}\n')
    print('Changes save successfully')
    file.close()
    

expenses = load_expense()

while True:
    print('===== EXPENSE SAVER =====')
    print('1. View Expense')
    print('2. Add Expense')
    print('3. Search Expense')
    print('4. Delete Expense')
    print('5. Show Total')
    print('6. Save Expenses')
    print('7. Exit')
    print('=========================')

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
        save_expenses(expenses)

    elif choice == '7':
        print('Thank you for using Expense Saver')
        break

    else:
        print('Invalid choice!')