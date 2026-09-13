laptop = 10
keyboard = 15
mouse = 20

while True:
    print('==========INVENTORY==========')
    print('1. View Stock')
    print('2. Add Stock')
    print('3. Sell item')
    print('4. Exit')
    print('=============================')

    choice = input('Input Action:  ')
    if choice == '1':
        if laptop <= 5:
            print(f'Laptop : {laptop} LOW STOCK!')
        else:
            print(f'Laptop: {laptop}')
     
        if mouse <= 5:
            print(f'Mouse: {mouse} LOW STOCK!')
        else:
            print(f'Mouse: {mouse}')
        
        if keyboard  <= 5:
            print(f'Keyboard: {keyboard} LOW STOCK!')
        else:
            print(f'Keyboard: {keyboard}')
    elif choice == '2':
        print('===========================')
        enter_item = input('Choose Item:  ')
        print('---------------------------')
        if enter_item == '1':
            add_item = int(input('How many item to add ? :'))
            print('--------------------------')
            laptop += add_item
            print(f'{add_item} added to Laptop stock')
        elif enter_item == '2':
            add_item = int(input('How many item to add ? :'))
            print('--------------------------')
            mouse += add_item
            print(f'{add_item} added to mouse stock')
        elif enter_item == '3':
            add_item = int(input('How many item to add ? :'))
            print('--------------------------')
            keyboard += add_item
            print(f'{add_item} added to keyboard stock')
        else:
            print('Invalid Input')

    elif choice == '3':
        enter_item = input('choose item: ')
        if enter_item == '1':
            sell_item = int(input('How many item to sell ?: '))
            print('--------------------------')
            if sell_item <= laptop:
                laptop -= sell_item
                print(f'sold {sell_item} laptop/s')
                print(f'remaining stock: {laptop}')
            else:
                print('--------------------------')
                print('Not enough stock!')
        elif enter_item == '2':
            sell_item = int(input('How many item to sell ?: '))
            print('--------------------------')
            if sell_item <= mouse:
                mouse -= sell_item
                print(f'sold {sell_item} mouse')
                print(f'remaining stock: {mouse}')
            else:
                print('--------------------------')
                print('Not enough stock!')
        elif enter_item == '3':
            sell_item = int(input('How many item to sell ?: '))
            print('--------------------------')
            if sell_item <= keyboard:
                keyboard -= sell_item
                print(f'sold {sell_item} keyboard/s')
                print(f'remaining stock: {keyboard}')
            else:
                print('--------------------------')
                print('Not enough stock')
        else:
            print('Invalid input!')

    elif choice == '4':
        print('Thank You for using Inventory System!')
        break

    

        





