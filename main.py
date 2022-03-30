import random

import generateData
import nearestNeigbor2
import nearestNeighbour
import displayTour
import Opt2
from nearestNeigbor2 import *
from krandom import *
import sys


def write_info(dis_mat):
    print("Instance name:", instance.name)
    print("Dimention:", instance.size)
    print("Distance Type:", instance.EdgeWeightType)
    print(displayTour.matPrint(dis_mat))



def write_results():
    # ścieżka
    print(path)
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
    print("EUC_2D, LOWER_DIAG_ROW, FULL_MATRIX (atsp)")
    option = input("option: ")
    newFile = generateData
    if option != "EUC_2D":
        try :
            minimum = int(input(" minimum distance: "))
            maximum = int(input(" maximum distance: "))
            newFile.generateData(int(dimension), int(seed), option, minimum, maximum)
        except ValueError:
            print("Wrong data, minimum and maximum will be default")
            newFile.generateData(int(dimension), int(seed), option)
    else:
        try:
            minimum = int(input(" minimum x & y range: "))
            maximum = int(input(" maximum x & y range: "))
            newFile.generateData(int(dimension), int(seed), option, minimum, maximum)
        except ValueError:
            print("Wrong data, minimum and maximum will be default")
            newFile.generateData(int(dimension), int(seed), option)




    if option != "FULL_MATRIX":
        file = 'TSP_Data/random_instance_file.tsp'
        instance = ReadData(file)
        size = instance.size
        dis_mat = instance.GetDistanceMat()
    else:
        file = 'TSP_Data/random_instance_file.atsp'
        instance = ReadData(file,True)
        size = instance.size
        dis_mat = instance.dis_mat



    write_info(dis_mat)
    print(instance.size)
    while True:
        alg = input("NN, k-NN, k-random, 2opt-NN, 2opt-rand, 2opt-kNN, or anything else to quit ")
        if alg == "NN":
            path,_ = nearestNeighbour.run(size, dis_mat, random.randint(0, size-1))
        elif alg == "k-NN":
            path = nearestNeigbor2.run(size, dis_mat)
        elif alg == "k-random":
            k = input('k:')
            path = krandom(size, dis_mat, int(k))
        elif alg == "2opt-NN":
            path,_ = nearestNeighbour.run(size, dis_mat, random.randint(0, size-1))
            print(path)
            path = Opt2.Opt2(instance,path)
        elif alg == "2opt-rand":
            k = input('k:')
            path = krandom(size, dis_mat, int(k))
            path = Opt2.Opt2(instance,path)
        elif alg == "2opt-kNN":
            path = nearestNeigbor2.run(size, dis_mat)
            path = Opt2.Opt2(instance,path)
        else:
            sys.exit(1)
        write_results()
elif len(sys.argv) == 2:
    file = sys.argv[1]
    if file[-4] == 'a':
        instance = ReadData(file,True)
        size = instance.size
        dis_mat = instance.dis_mat
    else:
        instance = ReadData(file)
        size = instance.size
        dis_mat = instance.GetDistanceMat()

    write_info(dis_mat)
    while True:
        alg = input("NN, k-NN, k-random, 2opt-NN, 2opt-rand, 2opt-kNN, or anything else to quit ")
        if alg == "NN":
            path,_ = nearestNeighbour.run(size, dis_mat, random.randint(0, size-1))
        elif alg == "k-NN":
            try:
                k = int(input("podaj k"))
            except:
                k = 100
            path = nearestNeigbor2.run(size, dis_mat,k)
        elif alg == "k-random":
            k = input('k:' )
            path = krandom(size, dis_mat, int(k))
        elif alg == "2opt-NN":
            path,_ = nearestNeighbour.run(size, dis_mat, random.randint(0, size-1))
            path = Opt2.Opt2(instance,path)
        elif alg == "2opt-rand":
            k = input('k:')
            path = krandom(size, dis_mat, int(k))
            path = Opt2.Opt2(instance,path)
        elif alg == "2opt-kNN":
            try:
                k = int(input("podaj k"))
            except:
                k = 100
            path = nearestNeigbor2.run(size, dis_mat,k)
            path = Opt2.Opt2(instance,path)
        else:
            sys.exit(1)
        write_results()




