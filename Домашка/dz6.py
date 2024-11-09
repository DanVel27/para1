class Task:
    def __init__(self, name, description, deadline, status):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.status = status


class TaskManager(Task):
    def add(self):
        print("Task added.")

    def remove(self):
        print("Task removed.")


task1 = Task("class", "create class named task", 5, "not done")
taskmanaager1 = TaskManager()
