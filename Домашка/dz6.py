class Task:
    def __init__(self, name, description, deadline, status):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.status = status

    def attack(self, char):
        print("This is", char.name, ", he has", char.health, "HP.")


class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
