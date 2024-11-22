class Character:
    def __init__(self, name):
        self.name = name
        self.__health = 100
        self.__energy = 100
        self.__weapon = None

    def attack(self):
        if self.__energy >= 10:
            self.__energy -= 10
            print(f"Атакует с помошью {self.__weapon}.")
        else:
            print(f"Недостаточно энергии для атаки")

    def take_damage(damage):
        damage.__health -= 10
        if damage.__health <= 0:
            print(f"Персонаж {damage.name} умер")

    def equip_weapon(weapon):
        weapon.__weapon = "меч"
        print(f"У {weapon.name}, есть {weapon.__weapon}.")

    def get_status(self):
        weapon_status = self.__weapon if self.__weapon else "Немає зброї"
        return f"Имя: {self.name}, количество здоров'я: {self.__health}, количество енергии: {self.__energy}, Оружие: {weapon_status}"


character1 = Character
character1.get_status()
