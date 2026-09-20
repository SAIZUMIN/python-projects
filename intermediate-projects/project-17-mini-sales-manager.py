sales = {
    'John': {
        'Sales': 5,
        'Total': 2500
    },
    'Mark': {
        'Sales': 8,
        'Total': 4000
    },
    'Anna': {
        'Sales': 6,
        'Total': 3000
    }
}

while True:
    print('===== SALES MANAGER =====')
    print('1. View Sales')
    print('2. Add Employee')
    print('3. Search Employee')
    print('4. Update Sales')
    print('5. Update Total')
    print('6. Delete Employee')
    print('7. Show Total Sales')
    print('8. Show Average Sales')
    print('9. Exit')
    print('=========================')

    choice = input('Enter choice: ')
    if choice == '9':
        print('Thank you for using Sales Manager!')
        break

    elif choice == '1':
        count = 0
        for sale in sales:
            count += 1
            print(f"{count}. {sale} - Sales: {sales[sale]['Sales']} - Total: {sales[sale]['Total']}")

    elif choice == '2':
        add_name = input('Enter name: ').title()
        if add_name in sales or add_name == '':
            print('Invalid Name!')
        else:
            add_sales = int(input('Enter sales: '))
            if add_sales <= 0:
                print('Invalid Sales must be greater than 0')
            else:
                add_total = int(input('Enter total: '))
                if add_total <= 0:
                    print('Invalid Total must be greater than 0')
                else:
                    sales[add_name] = {
                        'Sales': add_sales,
                        'Total': add_total
                    }
                print('Employee successfully added!')

    elif choice == '3':
        search_name = input('Enter name: ').title()
        if search_name in sales:
            print('Name found!')
            print(f"{search_name} - {sales[search_name]['Sales']} - {sales[search_name]['Total']}")
        else:
            print('Name not found!')

    elif choice == '4':
        enter_name = input('Enter name: ').title()
        if enter_name in sales:
            update_sales = int(input('Enter sales: '))
            print('Sales Updated successfully!')
            sales[enter_name]['Sales'] = update_sales
        else:
            print('Name not found!')

    elif choice == '5':
        enter_name = input('Enter name: ').title()
        if enter_name in sales:
            update_total = int(input('Enter total: '))
            print('Total updated successfully!')
            sales[enter_name]['Total'] = update_total

    elif choice == '6':
        enter_name = input('Enter name: ').title()
        if enter_name in sales:
            sales.pop(enter_name)
            print('Employee deleted successfully!')
        else:
            print('Name not found!')

    elif choice == '7':
        total = 0
        for sale in sales:
            total += sales[sale]['Total']
        print(f'Total Sales: {total}')

    elif choice == '8':
        total = 0
        count = 0
        for sale in sales:
            count += 1
            total += sales[sale]['Total']

        average_sales = total / count
        print(f'Average Sales: {average_sales:.2f}')

    else:
        print('Invalid choice')
        
                

