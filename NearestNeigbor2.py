import time
import copy
import numpy as np

start_time = time.time()
import sys
from readData import ReadData
import displayTour
import calcTour



class nearestNeighbor2():

    def __init__(self, file):

        self.file = file
        self.instance = ReadData(self.file)
        self.size = self.instance.size
        self.dis_mat = self.instance.GetDistanceMat()

        self.path = []
        self.best_path = []
        self.cities = []
        self.best_distance = 99999999

    def _write_info(self):
        """
        write info about instance
        """
        print("Instance name:", self.instance.name)
        print("Dimention:", self.size)
        print("Distance Type:", self.instance.EdgeWeightType)


        displayTour.matPrint(self.dis_mat)



    def run(self):
        """
        :param path_index - temporary path
        :param best_path - the best path from NN algorithm
        :param changed_path - copy of dis_mat with changed values
        :param distance - distance
        :return:
        """
        for start in range(0,self.size):

            start_point = start
            path_index = list()
            path_index.append(start_point)
            changed_path = copy.copy(self.dis_mat)
            for i in range(self.size):
                changed_path[i][i] = 999999999

            path_index.append( np.argmin(changed_path[start_point]))
            for i in range(self.size):
                changed_path[i][start_point] = 999999999

            distance = self.dis_mat[start_point][path_index[1]]
            i=2

            while i != self.size:
                last_element = path_index[-1]
                #zmiana ostatnio użytego elementu na maksymalny, żeby nie został użyty
                for j in changed_path:
                    j[last_element] = 999999999

                path_index.append( np.argmin(changed_path[last_element]))
                distance += self.dis_mat[last_element][path_index[-1]]
                i += 1


            distance += self.dis_mat[path_index[0]][path_index[-1]]

            if distance < self.best_distance:
                print(distance,"distance")
                self.best_distance = distance
                self.best_path = path_index
        self.cities= [1+ x for x in self.best_path]

    def write_results(self):

        displayTour.printPath(self.dis_mat,self.cities)
        print("rozwiązanie: ", calcTour.fc(self.dis_mat, self.cities))
        displayTour.EUCgraph(self.instance, self.cities)


if len(sys.argv) < 2:
    print("need inpute file")
    sys.exit(1)
t = nearestNeighbor2(sys.argv[1])
t._write_info()
t.run()
t.write_results()


