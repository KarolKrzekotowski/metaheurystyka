import generateData
from nearestNeighbour import *
from nearestNeigbor2 import *
from krandom import *


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
    # with open('TSP_Data/random_instance_file.tsp', 'r') as data:
    #     pass
    while True:
        alg = input("NN, k-NN, k-random, 2opt, or anything else to quit ")
        if alg == "NN":
            t = nearestNeighbour('TSP_Data/random_instance_file.tsp')
        elif alg == "k-NN":
            t = nearestNeigbor2('TSP_Data/random_instance_file.tsp')
        elif alg == "k-random":
            pass
        elif alg == "2opt":
            pass
        else:
            sys.exit(1)
        t.write_info()
        t.run()
        t.write_results()
elif len(sys.argv) == 2:

    while True:
        alg = input("NN, k-NN, k-random, 2opt, or anything else to quit ")
        if alg == "NN":
            t = nearestNeighbour(sys.argv[1])
        elif alg == "k-NN":
            t = nearestNeigbor2(sys.argv[1])
        elif alg == "k-random":
            pass
        elif alg == "2opt":
            pass
        else:
            sys.exit(1)
        t.write_info()
        t.run()
        t.write_results()



