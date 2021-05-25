from src import process

wafer = str(input('Wafer Option'))
choice = str(input("Choose in Show, Save, Show and Save: "))

print('Please wait...')
if wafer is 'all':
    process.all(choice)
else:
    process.wafer(wafer, choice)
