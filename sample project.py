#Python ShoppingMall Project :



class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class ShoppingMall:
    def __init__(self):
        self.products = {
            "electronics": [
                Product("Laptop", 50000, "electronics"),
                Product("Mobile", 20000, "electronics"),
                Product("Headphones", 2000, "electronics")
            ],
            "clothing": [
                Product("T-Shirt", 500, "clothing"),
                Product("Jeans", 1500, "clothing"),
                Product("Jacket", 2500, "clothing")
            ],
            "groceries": [
                Product("Milk", 50, "groceries"),
                Product("Bread", 30, "groceries"),
                Product("Eggs", 60, "groceries")
            ]
        }
        self.cart = []
        self.total_bill = 0

    def display_categories(self):
        print("\n--- Shopping Mall Categories ---")
        for category in self.products.keys():
            print(category.upper())

    def display_products(self, category):
        print(f"\n--- {category.upper()} Products ---")
        for index, product in enumerate(self.products[category], 1):
            print(f"{index}. {product.name} - ₹{product.price}")

    def add_to_cart(self, category, product_index):
        try:
            selected_product = self.products[category][product_index - 1]
            self.cart.append(selected_product)
            self.total_bill += selected_product.price
            print(f"{selected_product.name} added to cart!")
        except IndexError:
            print("Invalid product selection!")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty!")
            return

        print("\n--- Your Cart ---")
        for index, product in enumerate(self.cart, 1):
            print(f"{index}. {product.name} - ₹{product.price}")
        print(f"Total Bill: ₹{self.total_bill}")

    def remove_from_cart(self, product_index):
        try:
            removed_product = self.cart.pop(product_index - 1)
            self.total_bill -= removed_product.price
            print(f"{removed_product.name} removed from cart!")
        except IndexError:
            print("Invalid cart item!")

    def checkout(self):
        if not self.cart:
            print("Your cart is empty!")
            return

        print("\n--- Checkout ---")
        self.view_cart()
        confirm = input("Confirm purchase? (yes/no): ").lower()
        
        if confirm == 'yes':
            print("Purchase successful! Thank you for shopping.")
            self.cart.clear()
            self.total_bill = 0
        else:
            print("Purchase cancelled.")

def main():
    mall = ShoppingMall()

    while True:
        print("\n--- Shopping Mall Menu ---")
        print("1. View Categories")
        print("2. View Products")
        print("3. Add to Cart")
        print("4. View Cart")
        print("5. Remove from Cart")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            mall.display_categories()
        
        elif choice == '2':
            category = input("Enter category name: ").lower()
            if category in mall.products:
                mall.display_products(category)
            else:
                print("Invalid category!")
        
        elif choice == '3':
            category = input("Enter category name: ").lower()
            if category in mall.products:
                mall.display_products(category)
                product_index = int(input("Enter product number: "))
                mall.add_to_cart(category, product_index)
            else:
                print("Invalid category!")
        
        elif choice == '4':
            mall.view_cart()
        
        elif choice == '5':
            mall.view_cart()
            if mall.cart:
                product_index = int(input("Enter cart item number to remove: "))
                mall.remove_from_cart(product_index)
        
        elif choice == '6':
            mall.checkout()
        
        elif choice == '7':
            print("Thank you for visiting our Shopping Mall!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
