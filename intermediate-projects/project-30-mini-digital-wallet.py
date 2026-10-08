class DigitalWallet:
    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def show_wallet(self):
        print(f'=== DIGITAL WALLET ===')
        print(f'Owner: {self.owner}')
        print(f'Balance: {self.__balance}')
        print('======================')

    def deposit(self, amount: int):
        if amount <= 0:
            print('Invalid Amount!')
            return 

        self.__balance += amount
        print('Deposit successful!')

    def withdraw(self, amount: int):
        if amount <= 0:
            print('Invalid Amount!')
            return

        if amount > self.__balance:
            print('Insufficient Balance!')
            return

        self.__balance -= amount
        print('Withdraw successful!')

def get_balance(wallets: list[DigitalWallet], owner: str):
    for wallet in wallets:
        if wallet.owner.lower() == owner.lower():
            return wallet.get_balance()
    return None


def find_wallet(wallets: list[DigitalWallet], owner:str ):
        for wallet in wallets:
            if wallet.owner.lower() == owner.lower():
                return wallet
        return None

def get_wallet():
    try:
        return int(input('Enter amount:  '))
    except ValueError:
        print('Invalid Amount!')
        return None
    
wallet1 = DigitalWallet('Jodell', 5000)
wallet2 = DigitalWallet('Dale', 3000)
wallet3 = DigitalWallet('Jade', 7000)

wallets = [wallet1, wallet2, wallet3]
while True:
    print('=== DIGITAL WALLET ===')
    print('1. View Wallets')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Search Wallet')
    print('5. Check Balance')
    print('6. Exit')
    print('======================')

    choice = input('Enter choice: ')
    if choice == '1':
        for wallet in wallets:
            wallet.show_wallet()

    elif choice == '2':
        owner = input('Enter name: ')
        wallet = find_wallet(wallets, owner)

        if wallet is None:
            print('Name not found!')
            continue

        amount = get_wallet()

        if amount is not None:
            wallet.deposit(amount)

    elif choice == '3':
        owner = input('Enter name: ')
        wallet = find_wallet(wallets, owner)

        if wallet is None:
            print('Name not found!')
            continue

        amount = get_wallet()

        if amount is not None:
            wallet.withdraw(amount)

    elif choice == '4':
        owner = input('Enter name: ')
        wallet = find_wallet(wallets, owner)

        if wallet is None:
            print('Name not found!')
            continue

        wallet.show_wallet()

    elif choice == '5':
        owner = input('Enter name: ')
        wallet = find_wallet(wallets, owner)

        if wallet is None:
            print('Name not found!')
            continue

        amount = wallet.get_balance()
        print(f'Balance: {amount}')

    elif choice == '6':
        print('Thank you for using Digital Wallet')
        break

    else:
        print('Invalid choice!')