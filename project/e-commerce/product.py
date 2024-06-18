import user as u

class Item:

    def __init__(self, name, quantity, price) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price
    

class Product(Item):


    def __init__(self):
        self.products = []

    def add(self, user, name, quantity, price):
        if user.role != "admin":
            print("Only admin can add")
            return

        new_product = Item(name, quantity, price)

        if self.products:
            for product in self.products:
                if product.name == name:
                    product.quantity += quantity
                    return
                 
        self.products.append(new_product)
        print("Added")

    
    def display_product(self):
        if not self.products:
            print("No products in inventory.")

        else:
            print("Product List:")
            for product in self.products:
                print(f"{product.name} - Quantity: {product.quantity} - Price: {product.price}")
            print()  # Blank line for separation

    def remove(self, name):
        for index, product in enumerate(index, self.products):
            if product.name == name:
                del self.products[index] 

            else:
                print("Product not found")

    def update(self, index, product):
        product.name = input("Enter new name: ")
        self.products[index] = product

    def get_product(self, name):
        for index, product in enumerate(self.products):
            if product.name == name:
                self.update(index, product)
                return

        print("Product not found")  
    
        
product = Product()
admin1 = u.Admin("ankitlovanshi", "ankit@123gmail.com")
cust1 = u.Customer("Sourabh", "sourabh@123gmail.com")

product.add(admin1, "Boult Drift smart watch", 10, 1500)
product.add(cust1, "Realme 5 Pro", 5, 15000)

# product.add()
# product1.get_product("Boult Drift smart watch")

