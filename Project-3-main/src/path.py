import os #운영체제에서 제공되는 여러 기능을 파이썬에서 수행할 수 있게한다.


def path(): #함수 path는 '\\'로 나누어진 현재 작업경로를 확인 후 값과 값 사이에 '/'를 넣어 반환한다.
    p = '/'.join(os.getcwd().split("\\"))
    return p
