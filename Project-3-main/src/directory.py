import os #운영체제에서 제공되는 여러 기능을 파이썬에서 수행할 수 있게한다.

def create_folder(directory): #지정된 경로가 있는지의 여부를 판단
    try:
        if not os.path.exists(directory): #디렉토리가 존재하지 않는다면
            os.makedirs(directory) #디렉토리를 만든다.
    except OSError: #try절을 실행하는 동안 예외가 발생하면 except절에서 예외를 처리
        print('Error: Creating directory. ' + directory) #에러를 출력한다.
