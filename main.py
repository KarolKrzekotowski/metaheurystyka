import generateData
import nearestNeigbor2
import nearestNeighbour
from nearestNeighbour import *
from nearestNeigbor2 import *
from krandom import *
import sys


def write_info():
    print("Instance name:", instance.name)
    print("Dimention:", instance.size)
    print("Distance Type:", instance.EdgeWeightType)


def write_results():
    # ścieżka
    displayTour.printPath(dis_mat, path)
    # dystans
    print("rozwiązanie: ", calcTour.fc(dis_mat, path))
    # wykres
    if instance.getEdgeWeightType() == "EUC_2D":
        displayTour.EUCgraph(instance, path)


if len(sys.argv) == 1:
    print("generating file")
    dimension = input("dimension: ")
    seed = input("seed: ")
    print("EUC_2D, LOWER_DIAG_ROW, FULL_MATRIX")
    option = input("option: ")
    minimum = input(" minimum: ")
    maximum = input(" maximum: ")
    newFile = generateData
    newFile.generateData(int(dimension), int(seed), option, int(minimum), int(maximum))

    file = 'TSP_Data/random_instance_file.tsp'
    instance = ReadData(file)
    size = instance.size
    dis_mat = instance.GetDistanceMat()
    write_info()
    print(dis_mat)
    while True:
        alg = input("NN, k-NN, k-random, 2opt, or anything else to quit ")
        if alg == "NN":
            path = nearestNeighbour.run(size, dis_mat)
            print(path)
        elif alg == "k-NN":
            path = nearestNeigbor2.run(size, dis_mat)
        elif alg == "k-random":
            pass
        elif alg == "2opt":
            pass
        else:
            sys.exit(1)
        write_results()
elif len(sys.argv) == 2:
    file = sys.argv[1]
    instance = ReadData(file)
    size = instance.size
    dis_mat = instance.GetDistanceMat()
    write_info()
    while True:
        alg = input("NN, k-NN, k-random, 2opt, or anything else to quit ")
        if alg == "NN":
            path = nearestNeighbour.run(size, dis_mat)
        elif alg == "k-NN":
            path = nearestNeigbor2.run(size, dis_mat)

        elif alg == "k-random":
            pass
        elif alg == "2opt":
            pass
        else:
            sys.exit(1)
        write_results()




