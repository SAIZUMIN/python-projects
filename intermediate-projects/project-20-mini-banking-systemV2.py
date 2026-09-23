balance = 5000
transaction_count = 0
total_deposit = 0
total_withdraw = 0

def check_balance(balance):
    return balance

def deposit(balance, transaction_count, total_deposit):
    deposit_amount = int(input('Enter deposit amount: '))
    if deposit_amount <= 0:
        print('Invalid Amount!')
        return balance, transaction_count, total_deposit, False
    else:
        new_transaction_count = transaction_count + 1
        new_total_deposit = total_deposit + deposit_amount
        new_balance = balance + deposit_amount
        return new_balance, new_transaction_count, new_total_deposit, True
    
def withdraw(balance,  transaction_count, total_withdraw): 
    withdrawn_amount = int(input('Enter amount to withdraw: '))
    if withdrawn_amount <= 0 or withdrawn_amount > balance:
        print('Invalid Amount!')
        return balance, transaction_count, total_withdraw, False
    else:
        new_balance = balance - withdrawn_amount
        new_transaction_count = transaction_count + 1
        new_withdrawn_amount = total_withdraw + withdrawn_amount
    return new_balance, new_transaction_count, new_withdrawn_amount, True

def transaction_summary(balance, transaction_count, total_deposit, total_withdraw ):
    return(
    f'Current Balance: {balance}'
    f'\nTransaction: {transaction_count}'
    f'\nTotal Deposit: {total_deposit}'
    f'\nTotal Withdrawals: {total_withdraw}'
    )


while True:
    print('=====BANKING SYSTEM=====')
    print('1. Check Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Transaction Summary')
    print('5. Exit')
    print('========================')

    choice = input('Enter choice: ')
    if choice == '1':
        print(f'Current Balance: {check_balance(balance)}')

    elif choice == '2':
        balance, transaction_count, total_deposit, success = deposit(
             balance, transaction_count, total_deposit
        )
        if success:
            print('amount successfully deposit!')

    elif choice == '3':
        balance, transaction_count, total_withdraw, success = withdraw(
            balance, transaction_count, total_withdraw
        )
        if success:
            print('amount successfully withdrawn!')

    elif choice == '4':
        print('===== TRANSACTION SUMMARY =====')
        print(transaction_summary(
        balance, transaction_count, total_deposit, total_withdraw
        ))

    elif choice == '5':
        print('Thank you for using mini Banking System!')
        break

    else:
        print('Invalid choice!')