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

    def special_move(self):
        print(f"{self.name} used special move!")

    def health_manager(self, health):
        self.health = health

        def manage_health(amount):
            if amount == 0:
                health += amount
            return health

        return manage_health


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self):
        print("Added", self.name, "to inventory")

    def __iter__(self):
        for item in player.inventory:
            item = self.items

    def special_ability(func):
        def wrapper(self):
            if getattr(self, "_ability_uses", 3) > 0:
                self._ability_uses -= 1
                return func(self)
            else:
                print("Special ability has no uses left!")

        return wrapper


def find_item(inventory, item_name):
    for item in inventory:
        if item == item_name:
            yield item
    yield "Item not found"

character1 = Character("Grinch")
player = Player("Hero")
