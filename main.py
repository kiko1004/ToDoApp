#Task Manager
#Add Task function
#Show Task
#Checkbox
#Date and Label
#Deadline
#Priority list: optional
import datetime


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




if __name__ == "__main__":
    tsk_list = TaskList("Viktor", "daily")
    tsk = Task("Homework", "2023-07-15", datetime.datetime.today().date(), "It's important")
    tsk2 = Task("Homework2", "2023-08-25", datetime.datetime.today().date(), "You have time")
    tsk_list.add_task(tsk, tsk2)
    print(tsk_list)