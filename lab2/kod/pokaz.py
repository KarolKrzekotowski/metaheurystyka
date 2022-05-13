import random

from tabu2 import TabuSearch
import sys
import generateData
from readData import ReadData
import nearestNeigbor2
import Opt2
from Paths import fc, swap, invert
import nearestNeighbour

methods= {
    'swap': swap,
    'invert': invert
}
#losowa
if sys.argv[1] == 'nowy':
    #EUC_2D

    try:
        # dimension, seed, option, minimum, maximum = sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]
        x = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], int(sys.argv[5]), int(sys.argv[6])
    except:
        print("nowy, dimension, seed, option(FULL_MATRIX, LOWER_DIAG_ROW, EUC_2D), minimum, maximum")
        sys.exit(1)
    generateData.generateData(*x)

    if x[4] != "FULL_MATRIX":
        file = 'TSP_Data/random_instance_file.tsp'
        instance = ReadData(file)
        size = instance.size
        dis_mat = instance.GetDistanceMat()
    else:
        file = 'TSP_Data/random_instance_file.atsp'
        instance = ReadData(file,True)
        size = instance.size
        dis_mat = instance.dis_mat
    path = nearestNeigbor2.run(size, dis_mat, 0)
    path = Opt2.Opt2(instance, path, True)

else:
    if len(sys.argv) > 3:
        print("złe argumenty")
        sys.exit(1)
    file = sys.argv[1]
    if file[-4] == 'a':
        instance = ReadData(file, True)
        size = instance.size
        dis_mat = instance.dis_mat
    else:
        instance = ReadData(file)
        size = instance.size
        dis_mat = instance.GetDistanceMat()

    start = random.randint(0, size - 1)
    path, distance = nearestNeighbour.run(size, dis_mat, start)

    if len(sys.argv) == 3:
        if sys.argv[2] == '1':
            path = nearestNeigbor2.run(size, dis_mat, 0)
            path = Opt2.Opt2(instance, path, True)
        else:
            path =  nearestNeigbor2.run(size, dis_mat, 0)


distance = fc(dis_mat, path)
halo = TabuSearch(distance, path, dis_mat)
while True:
    func = input('invert/swap lub exit:')
    if func not in methods:
        sys.exit(0)



    (tabu_size) = int(input("rozmiar tabu "))
    iterations = int(input("ilość iteracji "))
    najlepsza = int(input("najlepsza możliwa "))
    halo.run(int(iterations), int(tabu_size),najlepsza, method=methods[func])




