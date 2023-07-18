class TaskList:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.lst = []

    def add_task(self, *task):
        self.lst.extend(task)

    def get_tasks(self):
        _str = f"{self.name}:\n"
        for index, task in enumerate(self.lst):
            _str += f"{index + 1}. {task}\n"
        return _str

    def __str__(self):
        return self.get_tasks()

class Task:
    def __init__(self, task_name, deadline, date, label):
        self.label = label
        self.date = date
        self.deadline = deadline
        self.task_name = task_name

    def __str__(self):
        return f"Task name: {self.task_name}, Deadline: {self.deadline}, Date: {self.date}, Label: {self.label}"
