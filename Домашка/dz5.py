class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, char):
        print("This is", char.name, ", he has", char.health, "HP.")


class Hero(Character):
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon


class Enemy(Character):
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage


character1 = Character("Jojo", 100)
hero1 = Hero("Joseph", 110, "sword")
enemy1 = Enemy("Dio", 300, 70)
character1.attack(enemy1)
character1.attack(hero1)
