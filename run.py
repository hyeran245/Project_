from src import process

while True:
    flag = False
    wafer = str(input('Wafer Option: '))
    coordinate = str(input('Coordinate Option: '))
    image = str(input("Choose in Show, Save, Show and Save: "))
    print('Please wait...')
    try:
        if wafer == 'all' and coordinate == 'all':
            process.all(image)
        elif wafer != 'all' and coordinate == 'all':
            process.wafer(wafer, image)
        else:
            process.coordinate(wafer, coordinate, image)
        while True:
            retry = input('Do you want to run again? (y/n): ')
            if retry == 'n':
                flag = True
                break
            elif retry == 'y':
                break
    except ValueError as e:
        print('Error: ', e, ', Pleas Input Again\n')
    if flag is True:
        break
