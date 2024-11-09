class Bicycle:
    def __init__(self):
        self.brand = "bread"
        self.model = "3y"
        self.year = 2017

    def get_age(self):
        return 2024 - self.year


bicycle1 = Bicycle()
bicycle1.get_age()


class Doctor:
    def __init__(self, name):
        self.name = name


class Patient:
    def __init__(self, name):
        self.name = name

    def introduce_doctor(self, doctor):
        print(f"My doctor name is {doctor.name}")


doctor1 = Doctor("Mr.puk")
patient1 = Patient("Ivan Ivanovich")
patient1.introduce_doctor(doctor1)


class Vehicle:
    def move(self):
        print("Vehicle moves")


class Car(Vehicle):
    def move(self):
        print("Car drives")


my_vehicle = Car()
my_vehicle.move()


class Pen:
    def write(self):
        print("Writing")


class Highlighter:
    def highlight(self):
        print("Highlighting")


class Marker(Pen, Highlighter):
    pass


my_marker = Marker()
my_marker.write()
my_marker.highlight()
