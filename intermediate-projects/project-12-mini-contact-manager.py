names = ['John', 'Mark', 'Anna']
phones = ["09123456789", "09234567890", "09345678901"]

while True:

    print('=====CONTACT MANAGER=====')
    print('1. View Contact')
    print('2. Add Contact')
    print('3. Search Contact')
    print('4. Update Contact')
    print('5. Delete Contact')
    print('6. Exit')
    print('=========================')

    choice = input('Enter choice: ')
    if choice == '6':
        print('Thank You for using Mini Contact Manager. Goodbye!')
        break

    elif choice == '1':
        print(f'=====CONTACTS=====')
        for i in range(len(names)):
            print(f'{i+1}. {names[i]} - {phones[i]}')
        print('===================')

    elif choice == '2':
        print('===================')

        add_contact_name = input('Enter contact name: ')
        if add_contact_name == '':
            print('Invalid contact name')
        elif add_contact_name != '':
            add_contact_number = input('Enter contact number: ')
            if add_contact_number != '' and len(add_contact_number) == 11:

                names.append(add_contact_name)
                phones.append(add_contact_number)

                print('Contact added successfully!')
                
            else:
                print('Invalid phone number')

    elif choice == '3':

        print('====================')
        search_contact = input('Enter contact name to search: ').title()
        if search_contact in names:
            position = names.index(search_contact)
            print(f'name found contact number: {phones[i]}')
        else:
            print('name not found in contacts!')

    elif choice == '4':

        print('====================')
        enter_name = input('Enter contact name: ').title()
        if enter_name in names:
            position = names.index(enter_name)

            enter_new_phonenumber = input('Enter new phone number: ')
            if enter_new_phonenumber != '' and len(enter_new_phonenumber) == 11:
                phones[position] = enter_new_phonenumber

                print('Contact number successfully updated!')
            else:
                print('Invalid phone number')
        else:
            print('Inputed name not in contacts!')

    elif choice == '5':

        print('====================')
        enter_name = input('Enter contact name: ').title()
        if enter_name in names:
                position = names.index(enter_name)

                names.pop(position)
                phones.pop(position)

                print('Contact deleted successfully!')

    else:
        print('Invalid choice!')


        
            
