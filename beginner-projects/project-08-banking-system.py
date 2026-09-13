username = 'admin'
password = '12345'
balance = 5000
attempt = 0
transaction = 0
total_deposit = 0
total_withdrawals = 0

while True:
    enter_username = input('Enter username:  ')
    enter_password = input('Enter password:  ')

    if password == enter_password and username == enter_username:
        print('----------------------')
        print('Login Successful')

        while True:
            print('==========BANK==========')
            print('1. Check Balance')
            print('2. Deposit')
            print('3. Withdraw')
            print('4. Transaction Summary')
            print('5. Logout')
            print('========================')

            choice = input('Enter action:  ')
            print('========================')
            if choice == '1':
                print(f'Current balance: {balance}')

            elif choice == '2':
                enter_amount = int(input('Enter amount to deposit: '))
                if enter_amount > 0:
                    balance += enter_amount
                    transaction += 1
                    total_deposit += enter_amount

                    print('----------------------------------')
                    print(f'Deposit: {enter_amount} ')
                    print(f'New Balance: {balance}')

                else:
                    print('-----------------------------------')
                    print('Deposit amount must be greater than 0')

            elif choice == '3':
                enter_withdraw_amount = int(input('Enter amount to withdraw: '))

                if enter_withdraw_amount > 0 and enter_withdraw_amount <= balance and total_withdrawals + enter_withdraw_amount <= 5000:
                    balance -= enter_withdraw_amount
                    transaction += 1
                    total_withdrawals += enter_withdraw_amount

                    print('-----------------------------------')
                    print(f'Withdraw: {enter_withdraw_amount}')
                    print(f'Remaining balance: {balance}')

                elif total_withdrawals + enter_withdraw_amount > 5000:
                    print('Withdrawal exceeds Daily limit!')

                else:
                    print('-----------------------------------')
                    print('withdraw amount must be greater than 0 and less than balance')
          
            elif choice == '4':
                print('===========SUMMARY==========')
                print(f'Balance: {balance}')
                print(f'Transactions: {transaction}')
                print(f'Total Deposits: {total_deposit}')
                print(f'Total Withdrawals: {total_withdrawals}')

            elif choice == '5':
                print('-----------------------------------')
                print('Logout successfuly!')
                break

            else:
                print('-----------------------------------')
                print('Invalid choice')        
    else:
        attempt += 1
        print('Wrong password or username')
    if attempt == 3:
        print('Account locked')
        break

    
