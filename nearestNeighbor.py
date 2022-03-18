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
        self.changed_path = self.instance.GetDistanceMat()
        self.path =[]
        self.cities = []

    def _write_info(self):
        """
        write info about instance
        """
        # print("Instance name:", self.instance.name)
        # print("Dimention:", self.size)
        # print("Distance Type:", self.instance.EdgeWeightType)
        # print(self.dis_mat)

        # displayTour.matPrint(self.dis_mat)
        #


    def run(self):
        start_point = random.randint(1, self.size)


        path_index = list()
        path_index.append(start_point)
        changed_path = self.changed_path
        for i in range(self.size):
            changed_path[i][i] = 999999999


        path_index.append( np.argmin(changed_path[start_point-1]))
        for i in range(self.size):
            changed_path[i][start_point-1]


        distance = self.dis_mat[start_point-1][path_index[1]]
        i=1
        self.cities.append(start_point)
        self.cities.append(np.argmin(changed_path[start_point-1])+1)


        while i != self.size:
            last_element = path_index[-1]
            #zmiana ostatnio użytego elementu na maksymalny, żeby nie został użyty
            for j in changed_path:
                j[last_element] = 999999999

            path_index.append( np.argmin(changed_path[last_element]))

            distance += self.dis_mat[last_element][path_index[-1]]

            self.cities.append(np.argmin(changed_path[last_element])+1)
            i += 1

        print("lista", path_index)

        print(distance,"distance")
        self.path = path_index


    def write_results(self):

        displayTour.printPath(self.dis_mat,self.cities)
        # print(self.path)


        print("rozwiązanie: ", calcTour.fc(self.dis_mat, self.cities))
        print(self.cities)
        displayTour.EUCgraph(self.instance, self.path)



if len(sys.argv) < 2:
    print("need inpute file")
    sys.exit(1)
t = nearestNeighbor(sys.argv[1])
t._write_info()
t.run()
t.write_results()


