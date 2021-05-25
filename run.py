from src import process

option = str(input())
choice = str(input("What you gonna do?\n"
                   "Choose in Show, Save, Show and Save: "))

if option is None:
    process.all(choice)
else:
    process.wafer(option, choice)
print('Please wait...')