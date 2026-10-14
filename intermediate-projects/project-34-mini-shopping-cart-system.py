class Product:
    def __init__(self, name: str,price: int):

        if type(price) is not int or price <= 0:
            raise ValueError('Invalid price must be greater than 0')

        if type(name) is not str or not name.strip():
            raise ValueError('Invalid product name ')
        
        self.name = name
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
            print('Invalid product: Expected a Product object')
            return

        if type(quantity) is not int or quantity <= 0:
            print('Quantity must be a positive whole number')
            return

        for item in self.items:
            if item.product == product:
                item.quantity += quantity
                print('Quantity added')
                return 
            
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
            print('Invalid product: Expected a Product object')
            return

        if type(new_quantity) is not int or new_quantity <= 0:
            print('Quantity must be a positive whole number')
            return

        for item in self.items:
            if item.product == product:
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
            print('Invalid product: Expected a Product object')
            return

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
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self) -> int:
        return self.product.price * self.quantity

    


# --- Section 1: Product Setup & Subtotal Test ---
try:
    product1 = Product('Keyboard', 850)
    product2 = Product('Mouse', 450)
    product3 = Product('Monitor', 5500)
    
    sub = CartItem(product1, 2)
    print("CartItem Subtotal:", sub.calculate_subtotal())
except ValueError as e:
    print(f"[Error in Setup/Subtotal]: {e}")


try:
    cart = ShoppingCart()
    cart.add_item(product1, 2)
    cart.add_item(product1, 3)
    cart.add_item(product2, 3)
    cart.add_item(product1, 2) 
    cart.add_item("Keyboard", 2)
    cart.add_item(None, 2)   
    cart.add_item(product1, 0)
    cart.add_item(product1, 2.5)
    cart.display_cart()
    
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