# from abc import ABC, abstractmethod


class GameCharacter():
    #@abstractmethod
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
