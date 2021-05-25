from src import process

wafer = str(input('Wafer Option: '))
coordinate = str(input('Coordinate Option: '))
choice = str(input("Choose in Show, Save, Show and Save: "))

print('Please wait...')
if wafer == 'all' and coordinate == 'all':
    process.all(choice)
elif wafer != 'all' and coordinate == 'all':
    process.wafer(wafer, choice)
else:
    process.coordinate(wafer, coordinate, choice)