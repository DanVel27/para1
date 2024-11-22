from abc import ABC, abstractmethod



class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass


class Warrior(GameCharacter):
    def attack(self):
        return "Sword"


class Mage(GameCharacter):
    def attack(self):
        return "Magic"


warrior1 = Warrior()
mage1 = Mage()
print(warrior1.attack())
print(mage1.attack())


class PlayerInventory:
    def __init__(self, items):
        self.__items = items

    def add_item(self, item):
        if item > 0:
            self.__items += item

    def remove_item(self, item):
        if item > 0:
            self.__items -= item
        else:
            print("No items in inventory")

    def show_inventory(self):
        print(self.__items)


player1 = PlayerInventory(1)
player1.show_inventory()
player1.add_item(4)
player1.show_inventory()
player1.remove_item(2)
player1.show_inventory()
