inventory = {
    'Laptop': 5,
    'Keyboard': 10,
    'Mouse': 15
}

def view_inventory(inventory):
        for inv in inventory:
            print(f"{inv} - {inventory[inv]}")


def add_stock(inventory):
     new_product = input('Enter new product: ').title()
     if new_product in inventory:
          print('Product already exist!')
     else:
        product_quantity = int(input('Enter product quantity: '))
        if product_quantity <= 0 :
             print('Invalid Quantity must be greater than 0')
        else:
             print('Product added successfully!')
             inventory[new_product] = product_quantity

def sell_product(inventory):
    sell = input('Enter Product to sell: ').title()
    if sell not in inventory:
         print('Product not found!')
    else:
        sell_quantity = int(input('Enter product quantity to sell: '))
        if sell_quantity > inventory[sell]:
            print('Cannot sell more than available stock!')
        elif sell_quantity <= 0:
            print('Quantity must be greater than 0!')
        else:
            inventory[sell] -= sell_quantity      
            print('Product sold successfully!')

def search_product(inventory):
    search = input('Enter product name: ').title()
    if search in inventory:
          print('Product Found!')
          print(f'Product: {search}')
          print(f'Stock: {inventory[search]}')
    else:
         print('Product not found!')


def total_items(inventory):
    add = 0
    for inv in inventory:
        add += inventory[inv]
    print(f'Total Items: {add}')


while True:
    print('===== INVENTORY SYSTEM =====')
    print('1. View Inventory')
    print('2. Add Stock')
    print('3. Sell Product')
    print('4. Search Product')
    print('5. Show Total Items')
    print('6. Exit')
    print('============================')

    choice = input('Enter choice: ')
    if choice == '6':
        print('Thank you for using Inventory System!')
        break

    elif choice == '1':
      view_inventory(inventory)

    elif choice == '2':
       add_stock(inventory)

    elif choice == '3':
       sell_product(inventory)

    elif choice == '4':
        search_product(inventory)

    elif choice == '5':
        total_items(inventory)

    else:
        print('Invalid Choice!')
         
         