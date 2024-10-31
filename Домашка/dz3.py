class Product:
    def __init__(self):
        self.name = "bread"
        self.price = 5
        self.quantity = 50
        self.calculate_total_price = self.price * self.quantity

    def display_info(self):
        print(f"{self.name} cost {self.price} dollar, and all cost {self.calculate_total_price}.")

product1 = Product()
product1.display_info()
