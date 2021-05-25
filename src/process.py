import glob
from glob import glob
from tqdm import tqdm
from . import path
from . import graph
from . import extract


def all(choice):
    for data in tqdm(glob(path.path() + '/data/**/*LMZ*.xml', recursive=True)):
        try:
            graph.graph(data, choice)
            extract.data_save(data)
        except:
            pass


def wafer(wafer, choice):
    for data in tqdm(glob(path.path() + '/data/**/{}/**/*LMZ*.xml'.format(wafer), recursive=True)):
        try:
            graph.graph(data, choice)
            extract.data_save(data)
        except:
            pass