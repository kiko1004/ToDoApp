import requests


def run():
    print("New Tasklist(+)\n"
          "Show existing tasklist(<*>)\n"
          "Save progess(_^_)\n"
          "Load project(-->)\n")

    tasklists = []

    while True:
        tasklists = requests.Requests.request_responding(tasklists)