import csv
import numpy as np


salammbo_a_en = "A2/salammbo_a_en.tsv"
salammbo_a_fr = "A2/salammbo_a_fr.tsv"

def load_data(file):
    x = []
    y = []
    with open(file) as fd:
        rd = csv.reader(fd, delimiter="\t", quotechar='"')
        for row in rd:
            x.append(int(row[0]))
            y.append(int(row[1]))
    x = normalize(x)
    y = normalize(y)
    return x, y



def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm

    

x, y = load_data(salammbo_a_fr)
#load_data(salammbo_a_fr)
#x = normalize(x)
#y = normalize(y)
X = np.column_stack((x, y))
#perc_data()
print(X)
