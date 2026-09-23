users = {
    'John': {
        'Password': '1234',
        'Balance': 5000
    },
    'Mark': {
        'Password': '5678',
        'Balance': 3000
    },
    'Anna': {
        'Password': '9999',
        'Balance': 7000
    }
}
def view_user(users):
    number = 0
    for user in users:
        number += 1
        print(f"{number}. {user} - {users[user]['Balance']}")

def add_user(users):
    new_name = input('Enter Username: ').title()
    if new_name in users:
        print('Username already exist!')
    elif new_name == '':
        print('Username is empty!')
    else:
        new_password = input('Enter Password: ')
        if new_password == '':
            print('Password is empty!')
        else:
            new_balance = int(input('Enter balance: '))
            if new_balance >= 0:
                users[new_name] = {
                    'Password': new_password,
                    'Balance': new_balance
                    }
                print('User successfully added!')
            else:
                print('Invalid balance! must be greater than or equual 0')

def login(users):
    enter_user = input('Enter Username: ').title()
    enter_password = input('Enter Password: ')
    if enter_user in users and users[enter_user]['Password'] == enter_password:
        print('Login successfull!')
        return True
    else:
        print('Invalid Username or Password')
        return False
    

def deposit(users):
    enter_user = input('Enter Username: ').title()
    if enter_user in users:
        deposit_amount = int(input('Enter deposit amount: '))
        if deposit_amount > 0:
            print('Deposit Successfull!')
            users[enter_user]['Balance'] += deposit_amount
        else:
            print('Invalid Amount!')
    else:
        print('User not found!')

def withdraw(users):
    enter_user = input('Enter username: ').title()
    if enter_user in users:
        withdraw_amount = int(input('Enter withdraw amount: '))
        if withdraw_amount > users[enter_user]['Balance'] or withdraw_amount <= 0:
            print('Invalid Amount!')
        else:
            print('Amount withdraw successfully!')
            users[enter_user]['Balance'] -= withdraw_amount
    else:
        print('User not found!')

def search_user(users):
    enter_user = input('Enter Username: ').title()
    if enter_user in users:
        print('User found!')
        print(
            f'Username: {enter_user}'
            f"\nBalance: {users[enter_user]['Balance']}"
        )
    else:
        print('User not found!')

def delete_user(users):
    enter_username = input('Enter Username: ').title()
    if enter_username in users:
        users.pop(enter_username)
        print('User successfully deleted!')
    else:
        print('User not found')




while True:
    print('===== USER ACCOUNT SYSTEM =====')
    print('1. View User')
    print('2. Add User')
    print('3. Login')
    print('4. Deposit')
    print('5. Withdraw')
    print('6. Search User')
    print('7. Delete User')
    print('8. Exit')
    print('===============================')

    choice = input('Enter choice: ')
    if choice == '8':
        print('Thank you for using User Account System!')
        break

    elif choice == '1':
        view_user(users)

    elif choice == '2':
        add_user(users)

    elif choice == '3':
        if login(users):
            print('Welcome!')

    elif choice == '4':
        deposit(users)

    elif choice == '5':
        withdraw(users)

    elif choice == '6':
        search_user(users)

    elif choice == '7':
        delete_user(users)

    else:
        print('Invalid choice!')

