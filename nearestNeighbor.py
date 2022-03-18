import imp
import time

import numpy
import numpy as np

start_time = time.time()
import sys
from readData import ReadData
import displayTour
import calcTour
import random

class nearestNeighbor():

    def __init__(self, file):

        self.file = file
        self.instance = ReadData(self.file)
        self.size = self.instance.size
        self.dis_mat = self.instance.GetDistanceMat()

    def _write_info(self):
        """
        write info about instance
        """
        print("Instance name:", self.instance.name)
        print("Dimention:", self.size)
        print("Distance Type:", self.instance.EdgeWeightType)
        print(self.dis_mat)

        # displayTour.matPrint(self.dis_mat)
        #
        # #test cykli
        # bestpath = displayTour.loadPath(f'{self.instance.name}.opt.tour')
        #
        # if bestpath != None:
        #     displayTour.printPath(self.dis_mat,bestpath)
        #     print("rozwiązanie: ",calcTour.fc(self.dis_mat,bestpath))
        #     displayTour.EUCgraph(self.instance,bestpath)

    def run(self):
        start_point = random.randint(1, self.size)


        path_index = list()
        path_index.append(start_point)
        for i in range(self.size):
            self.dis_mat[i][i] = 999999999
        changed_path = self.dis_mat

        path_index.append( np.argmin(self.dis_mat[start_point-1]))
        print(self.dis_mat[start_point - 1][path_index[1]],'hello')
        distance = self.dis_mat[start_point-1][path_index[1]]
        i=1
        while i != self.size:
            last_element = path_index[-1]
            #zmiana ostatnio użytego elementu na maksymalny, żeby nie został użyty
            for j in changed_path:
                j[last_element] = 999999999

            path_index.append( np.argmin(changed_path[last_element]))
            distance += self.dis_mat[last_element][path_index[-1]]
            print(distance)
            i += 1

        print("lista", path_index)
        path_index.sort()
        print(path_index)
        print(distance,"distance")
        print(changed_path,"duże")



if len(sys.argv) < 2:
    print("need inpute file")
    sys.exit(1)
t = nearestNeighbor(sys.argv[1])
t._write_info()
t.run()

