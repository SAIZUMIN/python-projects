class BankAccount:
    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print(f"{self.name}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError
        else:
            self.balance += amount
            print('Deposit Successful!')
            print(f'New Balance: {self.balance}')

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError
        elif amount > self.balance:
            raise ValueError
        else:
            self.balance -= amount
            print('Withdrawal Successful!')
            print(f'New Balance: {self.balance}')

    def show_account(self):
        print('===== ACCOUNT =====')
        print(f'Name: {self.name}')
        print(f'Balance: {self.balance}')
        print('===================')

account = BankAccount('Jodell', 5000)

while True:
    print('===== BANK ACCOUNT =====')
    print('1. Show Account')
    print('2. Show Balance')
    print('3. Deposit')
    print('4. Withdraw')
    print('5. Exit')
    print('========================')

    choice = input('Enter choice: ')
    if choice == '1':
        account.show_account()

    elif choice == '2':
        account.show_balance()

    elif choice == '3':
        while True:
            try:
                amount = int(input('Enter amount: '))
                account.deposit(amount)
                break
            except ValueError:
                print('Invalid amount!')

    elif choice == '4':
        while True:
            try:
                amount = int(input('Enter amount: '))
                account.withdraw(amount)
                break
            except ValueError:
                print('Invalid amount')
            

    elif choice == '5':
        print('Thank you for using the Bank. bye!')
        break

    else:
        print('Invalid Choice!')
