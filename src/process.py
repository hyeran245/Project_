import glob
from glob import glob
from tqdm import tqdm
from . import path
from . import graph
from . import extract


def all(choice):
    for data in tqdm(glob(path.path() + '/data/P184640/**/*LMZ*.xml', recursive=True)):
        try:
            graph.graph(data, choice)
            extract.data_save(data)
        except:
            pass