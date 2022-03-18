import time
import copy
import numpy as np
from readData import ReadData
import displayTour
import calcTour
import random
start_time = time.time()

class nearestNeighbour():

    def __init__(self, file):

        self.file = file
        self.instance = ReadData(self.file)
        self.size = self.instance.size
        self.dis_mat = self.instance.GetDistanceMat()

        self.path =[]
        self.cities = []

    def write_info(self):
        """
        write info about instance
        """
        print("Instance name:", self.instance.name)
        print("Dimention:", self.size)
        print("Distance Type:", self.instance.EdgeWeightType)
        # displayTour.matPrint(self.dis_mat)

    def run(self):
        start_point = random.randint(0, self.size-1)
        path_index = [start_point]
        changed_path = copy.copy(self.dis_mat)
        for i in range(self.size):
            changed_path[i][i] = 999999999

        path_index.append( np.argmin(changed_path[start_point]))
        for i in range(self.size):
            changed_path[i][start_point] = 999999999

        distance = self.dis_mat[start_point][path_index[1]]
        i = 2

        while i != self.size:
            last_element = path_index[-1]
            # zmiana ostatnio użytego elementu na maksymalny, żeby nie został użyty
            for j in changed_path:
                j[last_element] = 999999999

            path_index.append( np.argmin(changed_path[last_element]))
            distance += self.dis_mat[last_element][path_index[-1]]

            i += 1

        path_index = [1 + x for x in path_index]
        self.path = path_index

    def write_results(self):
        # ścieżka
        displayTour.printPath(self.dis_mat,self.path)
        # dystans
        print("rozwiązanie: ", calcTour.fc(self.dis_mat, self.path))
        # wykres
        if self.instance.getEdgeWeightType() == "EUC_2D":
            displayTour.EUCgraph(self.instance, self.path)



