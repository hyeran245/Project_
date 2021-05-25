import glob
from glob import glob
from tqdm import tqdm
from . import path
from . import graph
from . import extract


def all(choice):
    for data in tqdm(glob(path.path() + '/data/**/*LMZ*.xml', recursive=True)):
        graph.graph(data, choice)
        extract.data_save(data)


def wafer(wafer, choice):
    flag = False
    for data in tqdm(glob(path.path() + '/data/**/{}/**/*LMZ*.xml'.format(wafer), recursive=True)):
        graph.graph(data, choice)
        extract.data_save(data)
        flag = True
    if flag is False:
        raise ValueError('Check Wafer Option')


def coordinate(wafer, coordinate, choice):
    flag = False
    for data in glob(path.path() + '/data/**/{}/**/*{}*LMZ*.xml'.format(wafer, coordinate), recursive=True):
        graph.graph(data, choice)
        extract.data_save(data)
        flag = True
    if flag is False:
        raise ValueError('Check Options')
