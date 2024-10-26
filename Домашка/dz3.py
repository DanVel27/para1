class Product:
    def __init__(self):
        self.name = "Bread"
        self.price = 30
        self.quatity = 5

    def printer(self):
        print(f"{self.name}{self.price}{self.quatity}")


product1 = Product()
product1.printer()
