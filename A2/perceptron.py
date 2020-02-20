import csv

def libsvm_reader(file):
    data = []
    with open(file) as f:
        for line in f:
            rows = line.strip().split()
            data.append([int(rows[0]), float(rows[1]), float(rows[2])])
    return data



print(libsvm_reader('A2/libsvm_data.libsvm'))