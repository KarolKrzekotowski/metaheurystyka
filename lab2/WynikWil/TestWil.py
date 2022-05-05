from os import readv
from scipy.stats import wilcoxon
import csv

def readVec(file):
    v0 = []
    v1 = []
    with open(file) as f:
        csv_reader = csv.reader(f,delimiter=',')
        for row in csv_reader:
            v0.append(float(row[0]))
            v1.append(float(row[1]))
    return v0,v1


def testWil(v1,v2):
    w,p = wilcoxon(v1,v2)
    print(w,p)

v0,v1 = readVec('data.csv')
testWil(v0,v1)
