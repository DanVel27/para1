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

    def mark(self):
        print("Done")


task1 = Task("class", "create class named task", 5, "not done")
taskmanager1 = TaskManager("class", "create class named task", 5, "not done")
task1.name()
taskmanager1.add()
