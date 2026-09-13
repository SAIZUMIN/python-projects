burger = 80
fries = 50
drink = 30
overall_total = 0

while True:
        print('==========STORE==========')
        print('1. burger - $80')
        print('2. fries - $50')
        print('3. drink - $30')
        print('4. Checkout')
        print("=========================")
        
        
        choice = input('choose an item: ')
        if choice == '1':
            number_of_burger = int(input('How many burgers you want ?: '))
            purchase = 80 * number_of_burger
            overall_total += purchase

        elif choice == '2':
            number_of_fries = int(input('How many fries do you want ?: '))
            purchase = 50 * number_of_fries
            overall_total += purchase

        elif choice == '3':
            number_of_drink = int(input('How many drinks do you want ? : '))
            purchase = 30 * number_of_drink
            overall_total += purchase

        elif choice == '4':     
            if overall_total >= 500:
                discount = overall_total * 0.20
                print('--------------------')
                print('20% \discount')

            elif overall_total >= 300 :
                discount = overall_total * 0.10
                print('--------------------')
                print('10% \discount')

            else:
                discount = 0
                print('--------------------')
                print('No discount')

            total = overall_total - discount
            print('======CHECKOUT======')
            print(f'Total: {overall_total}')
            print(f'Discount: {discount}')
            print(f'Final Total: {total}')
            print('====================')

            payment = int(input('Enter Payment: '))
            if payment < total:
                print('Insufficient Payment!')
            else:   
                change = payment - total
                print('=======================')
                print(f'Payment: {payment}')
                print(f'Final Total: {total}')
                print(f'Change: {change}')

                enter = input('\nEnter another Student? (Y/N): ')       
                overall_total = 0
                if enter.upper() != 'Y':
                    print('Thank you and Goodbye')
                    break
        else:
            print('Invalid choice')
        
                


    


    



        


