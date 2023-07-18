from tasklist import *
import datetime
import pickle




class Requests:

    def __init__(self, request_type : str):
        self.request_type = request_type

    @staticmethod
    def request_responding(tasklists: list):

        request_type = input("Enter request: ")


        if request_type == "New Tasklist":
            new_list = TaskList(input("Enter your tasklist name: "), input("Enter category: "))
            tasklists.append(new_list)

        elif request_type == "Show existing tasklist":
            if not tasklists:
                print("Tasklist is empty")

            for index, tasklist in enumerate(tasklists):
                print(f"{index + 1}. {tasklist.name} - {tasklist.category}")

            view_request = True if input("Would you like to view a tasklist?: Y/n:\n").lower() == "y" else False
            if view_request:
                view_task = int(input("Enter the number of the tasklist you would like to see: ")) - 1
                if view_task > len(tasklists) - 1:
                    print("Sorry this tasklist does not exist!")
                print(tasklists[view_task])

            change_req = True if input("Would you like to change a tasklist?: Y/n:\n").lower() == "y" else False
            if change_req:
                change_task = int(input("Enter the number of the tasklist you would like to change: ")) - 1
                if change_task > len(tasklists) - 1:
                    print("Sorry this tasklist does not exist!")
                new_task = Task(
                        task_name= input("Please enter taskname: "),
                        deadline= input("Enter deadline yyyy-mm-dd: "),
                        date= datetime.datetime.now().date(),
                        label= input("Enter note: ")
                    )
                tasklists[change_task].add_task(new_task)

        elif request_type == "Save progress":
            if not tasklists:
                print("Tasklist is empty!")
            with open(input("Enter projectname: ") + ".tl", 'wb') as handle:
                pickle.dump(tasklists, handle, protocol=pickle.HIGHEST_PROTOCOL)
                print("Project Saved")

        elif request_type == "Load project!":
            with open(input("Enter project: ") + '.tl', 'rb') as handle:
                tasklists = pickle.load(handle)
                print(tasklists)

        return tasklists



