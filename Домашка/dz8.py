class Character():
    def __init__(self, name):
        self.name = name

    def introduce(self, char):
        print("Character's name is", char.name)


class Player(Character):
    def __init__(self, inventory):
        self.inventory = inventory

    def introduce(self, playr):
        print("Player's name is", playr.name)


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(item):
        print("Added", item.name, "to inventory")


character1 = Character("Grinch")
