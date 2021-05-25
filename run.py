from src import process

choice = str(input("What you gonna do?\n"
                   "Choose in Show, Save, Show and Save: "))

process.all(choice)
