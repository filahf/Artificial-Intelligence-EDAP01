import csv
import numpy as np
x = []
y = []


with open("/home/filip/Documents/Artificial-Intelligence-EDAP01/ML/data/salammbo_a_en.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for row in rd:
        x.append(int(row[0]))
        y.append(int(row[1]))


def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


x = normalize(x)
y = normalize(y)
print(y)
