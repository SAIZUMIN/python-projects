class Product:
    def __init__(self, name: str,price: int):

        if type(price) is not int or price <= 0:
            raise ValueError('Invalid price must be greater than 0')

        if type(name) is not str or not name.strip():
            raise ValueError('Invalid product name ')
        
        self.name = name.strip()
        self.price = price

    def display_info(self):
        print('=== PRODUCT ===')
        print(f'Product: {self.name}')
        print(f'Price: ₱{self.price}')
        print('===============')

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product: Product, quantity : int) -> None:

        if not isinstance(product, Product):
            raise ValueError('Invalid product: Expected a Product object')

        if type(quantity) is not int or quantity <= 0:
            raise ValueError('Quantity must be a positive whole number')

        for item in self.items:
            if item.product == product:
                if (item.quantity + quantity) > 99:
                    raise ValueError('Product quantity cannot exceed 99')
                item.quantity += quantity
                print('Quantity added')
                return 
            
        if quantity > 99:
            raise ValueError('Product quantity cannot exceed 99')
            
        cart_item = CartItem(product, quantity)
        self.items.append(cart_item)

    def checkout(self) -> None:
        if not self.items:
            print('Your cart is empty')
            return

        print('=== CHECKOUT ===')
        self.display_cart()
        total = self.calculate_total()
        print(f'Total amount: ₱{total:,}')
        print('checkout successful')

        self.items.clear()

        

    def update_quantity(self, product: Product, new_quantity: int) -> None:
        if not isinstance(product, Product):
            raise ValueError('Invalid product: Expected a Product object')


        if type(new_quantity) is not int or new_quantity <= 0:
            raise ValueError('Quantity must be a positive whole number')
 

        for item in self.items:
            if item.product == product:
                if new_quantity > 99:
                    raise ValueError('Product quantity cannot exceed 99')
                item.quantity = new_quantity
                print('Quantity updated successfully')
                break
        else:
            print('Product isnt in the cart')

    
    def display_cart(self) -> None:
        print('=== SHOPPING CART ===')
        for item in self.items:
            print(f'Product: {item.product.name} - ₱{item.product.price} x {item.quantity} = ₱{item.calculate_subtotal():,} ')
        print('=====================')

    def calculate_total(self) -> int:
        total = 0
        for item in self.items:
            total += item.calculate_subtotal()
        return total

    def remove_item(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise ValueError('Invalid product: Expected a Product object')


        for item in self.items:
            if product == item.product:
                self.items.remove(item)
                print(f'{product.name.title()} removed from the cart')
                break
        else:
            print('Product isnt in the cart')

    def get_item_count(self) -> int:
        count = 0
        for item in self.items:
            count += item.quantity
        return count

    def clear_cart(self) -> None:
        self.items.clear()
        print('Cart cleared successfully')   

    def is_empty(self) -> bool:
        return not self.items
        

class CartItem:
    def __init__(self, product: Product, quantity: int) -> None:

        if type(quantity) is not int or quantity <= 0:
            raise ValueError ('Product must be a positive whole number')
    
        if quantity > 99:
            raise ValueError ('Product quantity cannot exceed 99')
        
        if not isinstance(product, Product):
            raise ValueError ('Invalid product: Expected a product object')
               
        self.product = product
        self.quantity = quantity
      
    def calculate_subtotal(self) -> int:
        return self.product.price * self.quantity

    
def test_invalid_cart_item(product, quantity, test_name):
    try:
        CartItem(product, quantity)
    except ValueError as e:
        print(f'PASS: {test_name} rejected - {e}')
    else:
        print(f'FAIL: {test_name} was accepted')


try:
    product1 = Product('Keyboard', 850)
    product2 = Product('Mouse', 450)
    product3 = Product('Monitor', 5500)
    
    test_invalid_cart_item(product1, -5, 'Negative quantity')
    test_invalid_cart_item(product1, 2.5, 'Decimal quantity')
    test_invalid_cart_item("Keyboard", 3, 'Invalid product')
    test_invalid_cart_item(product1, 0, 'Zero quantity')
    test_invalid_cart_item(product1, 100, 'Quantity above 99')
    test_invalid_cart_item(product1, '100', 'String quantity')
    
    sub = CartItem(product1, 2)
    print("CartItem Subtotal:", sub.calculate_subtotal())
    CartItem(product1, 1)
    CartItem(product1, 99)
    CartItem(product1, -5)
except ValueError as e:
    print(f"[Error in Setup/Subtotal]: {e}")

try:
    CartItem(product1, 2.5)
except ValueError as e:
    print(f'[Decimal quantity test]: {e}')

try:
    CartItem("Keyboard", 3)
except ValueError as e:
    print(f'[Product object test]: {e}')

try:
    CartItem(product1, 0)
except ValueError as e:
    print(f'[Invalid Quantity test]: {e}')

try:
    CartItem(product1, 100)
except ValueError as e:
    print(f'[Quantity exceeded test]: {e}')

try:
    CartItem(product1, '100')
except ValueError as e:
    print(f'[String quantity test]: {e}')



try:
    cart = ShoppingCart()
    cart.add_item(product1, 2)
    cart.add_item(product1, 99)

    total = cart.calculate_total()
    print(f'Total amount: {total:,}')
    print(f'Total item count: {cart.get_item_count()}')
except ValueError as e:
    print(f"[Error Adding Items]: {e}")

try:
    cart = ShoppingCart()
    cart.add_item(product1, 2)
    cart.add_item(product1, 97)

    total = cart.calculate_total()
    print(f'Total amount: {total:,}')
    print(f'Total item count: {cart.get_item_count()}')
except ValueError as e:
    print(f"[Error Adding Items]: {e}") 

try:
    cart = ShoppingCart()
    cart.add_item("Keyboard", 2)

    total = cart.calculate_total()
    print(f'Total amount: {total:,}')
    print(f'Total item count: {cart.get_item_count()}')
except ValueError as e:
    print(f"[Error Adding Items]: {e}")

try:
    cart = ShoppingCart()
    cart.add_item(product1, 2.5)

    total = cart.calculate_total()
    print(f'Total amount: {total:,}')
    print(f'Total item count: {cart.get_item_count()}')
except ValueError as e:
    print(f"[Error Adding Items]: {e}")

try:
    cart = ShoppingCart()
    cart.add_item(product1, 0)

    total = cart.calculate_total()
    print(f'Total amount: {total:,}')
    print(f'Total item count: {cart.get_item_count()}')
except ValueError as e:
    print(f"[Error Adding Items]: {e}")

try:
    cart = ShoppingCart()
    cart.add_item(None, 2)


    total = cart.calculate_total()
    print(f'Total amount: {total:,}')
    print(f'Total item count: {cart.get_item_count()}')
except ValueError as e:
    print(f"[Error Adding Items]: {e}")

try:
    product1.display_info()
    product2.display_info()
    product3.display_info()

    cart.checkout()
    cart.checkout() 
except ValueError as e:
    print(f"[Error in Checkout]: {e}")

try:
    cart.add_item(product3, 2)
    cart.clear_cart()
    cart.display_cart()
    print(f'Total amount: ₱{cart.calculate_total():,}')
    cart.add_item(product1, 2)
    print(cart.get_item_count())
    cart.add_item(product1, 0)
except ValueError as e:
    print(f"[Error in Clear/Total]: {e}")


try:
    empty_cart = ShoppingCart()
    empty_cart.remove_item(product1) 
    cart.remove_item("Keyboard")
    cart.update_quantity("Keyboard", 3)
except ValueError as e:
    print(f"[Error in Edge Case Test]: {e}")


try:
    print(f'Total item count: {cart.get_item_count()}')
    print("Is cart empty?", cart.is_empty())
except ValueError as e:
    print(f"[Error in Final Status]: {e}")

cart = ShoppingCart()
cart.add_item(product1, 98)

try:
    cart.add_item(product1, 2)
except ValueError as e:
    print(e)

print(cart.items[0].quantity)


print("\n=== TEST 1: UPDATE QUANTITY ===")

cart = ShoppingCart()
cart.add_item(product1, 5)

try:
    cart.update_quantity(product1, 100)
except ValueError as e:
    print("PASS: Invalid quantity rejected -", e)

if cart.items[0].quantity == 5:
    print("PASS: Previous quantity remains 5")
else:
    print("FAIL: Quantity changed unexpectedly")

cart.display_cart()


print("\n=== TEST 2: REMOVE ITEM ===")

cart = ShoppingCart()
cart.add_item(product1, 2)
cart.add_item(product2, 3)

cart.remove_item(product1)

if len(cart.items) == 1 and cart.items[0].product == product2:
    print("PASS: Keyboard removed; mouse remains")
else:
    print("FAIL: Incorrect product removal")

cart.display_cart()


print("\n=== TEST 3: CHECKOUT ===")

cart = ShoppingCart()
cart.add_item(product1, 2)
cart.add_item(product2, 3)

expected_total = (850 * 2) + (450 * 3)
actual_total = cart.calculate_total()

if actual_total == expected_total:
    print(f"PASS: Correct total - ₱{actual_total:,}")
else:
    print(f"FAIL: Expected ₱{expected_total:,}, got ₱{actual_total:,}")

cart.checkout()

if cart.is_empty() and cart.calculate_total() == 0:
    print("PASS: Cart emptied after checkout")
else:
    print("FAIL: Cart was not emptied")


print("\n=== TEST 4: VALID QUANTITY UPDATE ===")

cart = ShoppingCart()
cart.add_item(product1, 5)
cart.update_quantity(product1, 8)

if cart.items[0].quantity == 8:
    print("PASS: Quantity updated to 8")
else:
    print("FAIL: Quantity was not updated")


print("\n=== TEST 5: INVALID QUANTITY UPDATES ===")

cart = ShoppingCart()
cart.add_item(product1, 5)

for invalid_quantity in [0, -1, 100, 2.5, "8"]:
    try:
        cart.update_quantity(product1, invalid_quantity)
    except ValueError:
        pass

    if cart.items[0].quantity == 5:
        print(f"PASS: {invalid_quantity!r} rejected; quantity remains 5")
    else:
        print(f"FAIL: Cart quantity changed for {invalid_quantity!r}")

print("\n=== TEST 6: REMOVE PRODUCT ===")

cart = ShoppingCart()
cart.add_item(product1, 2)
cart.add_item(product2, 3)
cart.add_item(product3, 1)

cart.remove_item(product2)

remaining = {item.product.name: item.quantity for item in cart.items}

if remaining == {"Keyboard": 2, "Monitor": 1}:
    print("PASS: Correct product removed; other products unchanged")
else:
    print("FAIL:", remaining)

print("\n=== TEST 7: EMPTY CART ===")

cart = ShoppingCart()

if cart.is_empty() and cart.calculate_total() == 0 and cart.get_item_count() == 0:
    print("PASS: Empty cart has zero items and zero total")
else:
    print("FAIL: Empty cart returned unexpected values")

cart.checkout()

if cart.is_empty():
    print("PASS: Empty checkout handled correctly")
else:
    print("FAIL: Empty cart state changed")

print("\n=== TEST 8: SUCCESSFUL CHECKOUT ===")

cart = ShoppingCart()
cart.add_item(product1, 2)
cart.add_item(product2, 3)

expected_total = 3050

if cart.calculate_total() == expected_total:
    print("PASS: Total before checkout is correct")
else:
    print("FAIL: Total before checkout is incorrect")

cart.checkout()

if cart.is_empty() and cart.get_item_count() == 0 and cart.calculate_total() == 0:
    print("PASS: Cart cleared after checkout")
else:
    print("FAIL: Cart was not cleared correctly")

print("\n=== TEST 9: NEW ITEM QUANTITY LIMIT ===")

cart = ShoppingCart()

try:
    cart.add_item(product1, 100)
except ValueError:
    print("PASS: Quantity 100 rejected")
else:
    print("FAIL: Quantity 100 was accepted")

if cart.is_empty():
    print("PASS: Invalid addition did not change the cart")
else:
    print("FAIL: Cart changed unexpectedly")

print("\n=== TEST 10: SEPARATE PRODUCT OBJECTS ===")

cart = ShoppingCart()

keyboard_a = Product("Keyboard", 850)
keyboard_b = Product("Keyboard", 850)

cart.add_item(keyboard_a, 2)
cart.add_item(keyboard_b, 3)

print("Distinct cart entries:", len(cart.items))
print("Total quantity:", cart.get_item_count())