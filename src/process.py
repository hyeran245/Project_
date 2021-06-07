import glob
from glob import glob
from tqdm import tqdm
from . import path
from . import graph
from . import extract
import datetime
import os


now = datetime.datetime.now()
nowDatetime = now.strftime('%Y_%m_%d_%H_%M_%S')


def all(wafer, coordinate, save, show, csv, data_path):
    file = []
    flag = False
    if data_path == '':
        if wafer == 'All':
            file = glob(path.path() + '/data/**/*LMZ*.xml', recursive=True)
        elif wafer != 'All' and coordinate == '':
            file = glob(path.path() + '/data/**/{}/**/*LMZ*.xml'.format(wafer), recursive=True)
        elif wafer != 'All' and coordinate != 'All':
            file = glob(path.path() + '/data/**/{}/**/*{}*LMZ*.xml'.format(wafer, coordinate), recursive=True)
    else:
        if wafer == 'All':
            file = glob(data_path + '/**/*LMZ*.xml', recursive=True)
        elif wafer != 'All' and coordinate == '':
            file = glob(data_path + '/**/{}/**/*LMZ*.xml'.format(wafer), recursive=True)
        elif wafer != 'All' and coordinate != 'All':
            file = glob(data_path + '/**/{}/**/*{}*LMZ*.xml'.format(wafer, coordinate), recursive=True)
    for i in file:
        graph.graph(i, save, show, nowDatetime)
        if csv is True:
            extract.data_save(i, nowDatetime)
        flag = True
    if flag is False:
        raise ValueError('Could not find data')


def open():
    os.startfile(path.path() + '/result')
