#Task Manager
#Add Task function
#Show Task
#Checkbox
#Date and Label
#Deadline
#Priority list: optional
import datetime
import pickle


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
    tasklists = []
    while True:
        request = int(input("Create new tasklist(1) "
                            "or Show existing tasklists(2) "
                            "or Save progress(3) "
                            "or Load a project(4): 1 / 2 / 3 / 4:\n"))
        if request == 4:
            with open(input("Enter project: ") + '.tl', 'rb') as handle:
                tasklists = pickle.load(handle)

        if request == 3:
            if not tasklists:
                print("Tasklist is empty")
                continue

            with open(input("Enter project: ") + '.tl', 'wb') as handle:
                pickle.dump(tasklists, handle, protocol=pickle.HIGHEST_PROTOCOL)
                print("Project saved!")

        if request == 1:
            new_list = TaskList(input("Enter your tasklist name: "), input("Enter category: "))
            tasklists.append(new_list)
            continue
        elif request == 2:
            if not tasklists:
                print("Tasklist is empty")
                continue
            for index, tasklist in enumerate(tasklists):
                print(f"{index + 1}. {tasklist.name} - {tasklist.category}")

            view_request = True if input("Would you like to view a tasklist?: Y/n:\n").lower() == "y" else False
            if view_request:
                view_task = int(input("Enter the number of the tasklist you would like to see: ")) - 1
                if view_task > len(tasklists) - 1:
                    print("Sorry this tasklist does not exist!")
                    continue
                print(tasklists[view_task])

            change_req = True if input("Would you like to change a tasklist?: Y/n:\n").lower() == "y" else False
            if change_req:
                change_task = int(input("Enter the number of the tasklist you would like to change: ")) - 1
                if change_task > len(tasklists) - 1:
                    print("Sorry this tasklist does not exist!")
                    continue
                new_task = Task(
                    task_name= input("Please enter taskname: "),
                    deadline= input("Enter deadline yyyy-mm-dd: "),
                    date= datetime.datetime.now().date(),
                    label= input("Enter note: ")
                )
                tasklists[change_task].add_task(new_task)



