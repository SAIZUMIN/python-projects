#Dictionaries
products = {
    'Laptop': 30000,
    'Keyboard': 1500,
    'Mouse': 800
}


while True:
    print('=====PRODUCT MANAGER=====')
    print('1. View Product')
    print('2. Add Product')
    print('3. Search Product')
    print('4. Update Price')
    print('5. Delete Product')
    print('6. Exit')
    print('=========================')

    choice = input('Enter choice:  ')
    if choice == '6':
        print('Thank You for using Product Manager!')
        break

    elif choice == '1':
        counter = 0
        for product in products:
            counter += 1
            print(f'{counter}.  {product} - {products[product]}')
        print('===================')

    elif choice == '2':
        product_name = input('Enter product name:  ').title()
        if product_name in products:
            print('Product already exist')
        else:
            product_price = int(input('Enter product price: '))
            if product_price > 0:
                products[product_name] =  product_price
                print('')
                print(f'Product: {product_name} - {product_price} successfully added!')
            else:
                print('Invalid prodcut price!')

    elif choice == '3':
        product_name = input('Enter product name: ').title()
        if product_name in products:
                print('==================')
                print(f'{product_name} - {products[product_name]}')
        else:
            print(f'Product: {product_name} not in Inventory!')

    elif choice == '4':
        update_product = input('Enter product to update: ').title()
        if update_product in products:
            update_price = int(input('Enter new price: '))
            if  update_price > 0: 
                products[update_product] = update_price
                print(f'Product: {update_product} successfully updated!')
            else:
                print('Invalid product price!')
        else:
            print(f'Product: {update_product} not in Inventory')

    elif choice == '5':
        delete_product = input('Enter product name to delete: ').title()
        if delete_product in products:
            products.pop(delete_product)
            print(f'Product {delete_product} successfully deleted !')
        else:
            print(f'Product: {delete_product} not found!')
    else:
        print('Invalid choice')