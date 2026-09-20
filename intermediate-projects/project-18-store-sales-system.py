products = {
    'Laptop': {
        'Price': 30000,
        'Quantity': 5
    },
    'Keyboard': {
        'Price': 1500,
        'Quantity': 10
    },
    'Mouse': {
        'Price': 800,
        'Quantity': 15
    }
}

while True:
    print('=====STORE SALES SYSTEM=====')
    print('1. View Products')
    print('2. Add Product')
    print('3. Search Product')
    print('4. Update Price')
    print('5. Restock Product')
    print('6. Sell Product')
    print('7. Show Store Value')
    print('8. Exit')
    print('============================')

    choice = input('Enter choice: ')
    if choice == '8':
        print('Thank you for using Store Sales System!')
        break

    elif choice == '1':
        count = 0
        for product in products:
            count += 1
            print(
                f"{count}. {product} - Price: {products[product]['Price']} - "
                f"Stock: {products[product]['Quantity']}"
            )

    elif choice == '2':
        new_product = input('Enter new product name: ').title()
        if new_product in products or new_product == '':
            print('Invalid product name or product already exist!')
        else:
            new_price = int(input('Enter new product price: '))
            if new_price <= 0:
                print('Invalid Price!')
            else:
                new_quantity = int(input('Enter new product quantity: '))
                if new_quantity < 0:
                    print('Invalid Quantity')
                else:    
                    products[new_product] = {
                        'Price': new_price,
                        'Quantity': new_quantity
                    }
                    print('Product successfully added!')

    elif choice == '3':
        enter_product = input('Enter product name: ').title()
        if enter_product in products:
            print(f'Product: {enter_product}')
            print(f"Price: {products[enter_product]['Price']}")
            print(f"Stock: {products[enter_product]['Quantity']}")
        else:
            print('Product not found!')

    elif choice == '4':
        enter_product = input('Enter product name: ').title()
        if enter_product in products:
            new_price = int(input('Enter new product price: '))
            if new_price <= 0:
                print('Invalid Price!')
            else:
                products[enter_product]['Price'] = new_price
        else:
            print('Name not found!')

    elif choice == '5':
        product_name = input('Enter product name: ').title()
        if product_name in products:
            add_stock = int(input('Enter Quantity to add: '))
            if add_stock <= 0:
                print('Invalid Quantity!')
            else:
                products[product_name]['Quantity'] += add_stock
                print('Quantity added successfully!')
        else:
            print('Product not found!')

    elif choice == '6':
        product_name = input('Enter product name: ').title()
        if product_name in products:
            sell_product = int(input('Enter Quantity to sell: '))
            if sell_product <= 0:
                print('Invalid Quantity!')
            elif sell_product <= products[product_name]['Quantity']:
                print('Quantity successfully sold!')
                products[product_name]['Quantity'] -= sell_product
            else:
                print('Invalid Product Amount')
        else:
            print('Product not found!')

    elif choice == '7':
        overall_total = 0
        for product in products:
            total = products[product]['Price'] * products[product]['Quantity']
            overall_total += total
        print(f'Total Store Value: {overall_total}')

    else:
        print('Invalid Input')