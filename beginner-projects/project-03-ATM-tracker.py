balance = 5000
Pin = '1234'
attempt = 0
transactions = 0
total_deposit = 0
total_withdrawn = 0

while True:
    user = input('Enter Pin: ')
    if user == Pin:
        while True:
            print('======ATM======')
            print('1. Check Balance')
            print('2. Deposit')
            print('3. Withdraw')
            print('4. Transaction Summary')
            print('5. Exit')
            choice = input('Enter choice: ')
            print('------------------------------------------------')
            if choice == '5':
                print('Thank you for using the ATM Goodbye')
                break
            elif choice == '1':
                print(f'Current Balance: {balance}')
            elif choice == '2':
                enter_amount = int(input('Enter Deposit amount: '))
                if enter_amount > 0:
                    total_deposit += enter_amount
                    balance += enter_amount
                    transactions += 1
                    print(f'Deposit Amount: {enter_amount}')
                    print(f'Current Balance: {balance}')
                else:
                    print('Invalid')
            elif choice == '3':
                enter_withdraw_amount = int(input("Enter amount to withdraw:  "))
                if enter_withdraw_amount > 0 and enter_withdraw_amount <= balance and total_withdrawn + enter_withdraw_amount <= 5000:
                        balance -= enter_withdraw_amount
                        total_withdrawn += enter_withdraw_amount
                        transactions += 1
                        print(f'Withdrawn amount: {enter_withdraw_amount}')
                        print(f'Current Balance: {balance}')
                elif total_withdrawn + enter_withdraw_amount > 5000:
                    print('Daily withdrawal limit exceeded.')
                    remaining = 5000 - total_withdrawn
                    print(f'Remaining Withdrawal limit: {remaining}')
                elif enter_withdraw_amount <= 0:
                    print('Invalid Amount')
                else:
                    print('Insufficient balance.')
            elif choice == '4':
                print('==========Transaction Summary==========')
                print(f'Total transactions : {transactions}')
                print(f'Current Balance: {balance}')
                print(f'Total Deposit: {total_deposit}')
                print(f'Total Withdrawn: {total_withdrawn}')


        break
    else:
        print('------------------------------------')
        print('Incorrect PIN')
        attempt += 1
        if attempt == 3:
            print('Account Lock wait another hour')
            break

        
