class BankAccount:
    def __init__ (self, name: str, balance: int):
        self.name = name
        self.balance = balance

    def show_account(self):
        print('===== ACCOUNT =====')
        print(f'Name: {self.name}')
        print(f'Balance: {self.balance}')
        print('===================')

    def deposit(self, amount):
        if amount <= 0:
            print('Invalid!')
        else:
            print('Deposit successful!')
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print('Invalid!')
        elif amount > self.balance:
            print('Insufficient Balance!')
        else:
            self.balance -= amount
            print('Amount Withdraw successfully!')

    def transfer(self, amount, receiver):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                receiver.balance += amount
                print('Transfer successful!')
            else:
                print('Insufficient Balance!')
        else:
            print('Invalid!')

account1 = BankAccount('Jodell', 5000)
account2 = BankAccount('Dale', 3000)
account3 = BankAccount('Jade', 7000)

accounts = [account1, account2, account3]

while True:
    print('=== BANK TRANSFER ACCOUNT ===')
    print('1. View Accounts')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Transfer')
    print('5. Search Account')
    print('6. Exit')
    print('=============================')

    choice = input('Enter choice: ')
    if choice == '1':
        for account in accounts:
            account.show_account()

    elif choice == '2':
        name = input('Enter name: ').title()
        found = False
        for account in accounts:
            if name == account.name:
                found = True
                try:
                    amount = int(input('Enter amount: '))
                    account.deposit(amount)
                except ValueError:
                    print('Invalid!')
                    
        if not found:
            print('Name not found!')

    elif choice == '3':
        name = input('Enter name: ').title()
        found = False
        for account in accounts:
            if name == account.name:
                found = True
                try:
                    amount = int(input('Enter amount: '))
                    account.withdraw(amount)
                except ValueError:
                    print('Invalid!')
        if not found:
            print('Name not found!')

    elif choice == '4':
        sender = input('Enter name: ').title()
        found = False
        for account in accounts:
            if sender == account.name:
                sender_account = account
                found = True
                receiver = input('Enter receiver name: ').title()
                for account in accounts:
                    if receiver == account.name and receiver != sender:
                        receiver_account = account
                        try:
                            amount = int(input('Enter amount: '))
                            
                            sender_account.transfer(amount, receiver_account)
                        except ValueError:
                            print('Invalid!')
        if not found:
            print('Name not found!')

    elif choice == '5':
        name = input('Enter name: ').title()
        found = False
        for account in accounts:
            if name == account.name:
                found = True
                account.show_account()
        if not found:
            print('Name not found!')

    elif choice == '6':
        print('Thank you for using Bank Transfer')
        break

    else:
        print('Invalid choice!')