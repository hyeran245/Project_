import glob
from glob import glob
import graph
import extract
from tqdm import tqdm
import path

choice = str(input("What you gonna do?\n"
                   "Choose in Show, Save, Show and Save: "))

for data in tqdm(glob(path.path() + '/data/P184640/**/*LMZ*.xml', recursive=True)):
    try:
        graph.graph(data, choice)
        extract.data_save(data)
    except:
        pass