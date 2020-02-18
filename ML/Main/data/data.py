import csv
import numpy as np
x = []
y = []

salammbo_a_en = "ML/Main/data/salammbo_a_en.tsv"
salammbo_a_fr = "ML/Main/data/salammbo_a_fr.tsv"

def load_data(file):
    with open(file) as fd:
        rd = csv.reader(fd, delimiter="\t", quotechar='"')
        for row in rd:
            x.append(int(row[0]))
            y.append(int(row[1]))


def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm

load_data(salammbo_a_en)
load_data(salammbo_a_fr)
#x = normalize(x)
#y = normalize(y)
print(x)
