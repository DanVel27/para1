class Rectangle:
    def __init__(self):
        self.width = 7
        self.height = 4
        self.calculate_area = self.width * self.height
        self.calculate_perimeter = 2 * (self.width + self.height)

    def display_info(self):
        print(f"Area of rectangle is {self.calculate_area},and the perimeter is {self.calculate_perimeter}")


rectangle1 = Rectangle()
rectangle1.display_info()
