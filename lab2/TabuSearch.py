import tsplib95
import lab1.TSP.readData as readData
import lab1.TSP.nearestNeigbor2 as KNN
import lab1.TSP.calcTour as calcTour
import numpy as np
import  sys
np.concatenate

#neighbouring function


class TabuSearch:

    def __init__(self, bestdistance, path, dis_mat):
        self.path = path
        self.bestdistance = bestdistance
        self.dis_mat = dis_mat




if __name__ == '__main__':
    file = sys.argv[1]
    instance = readData.ReadData(file)
    size = instance.size
    dis_mat = instance.GetDistanceMat()
    path = KNN.run(size, dis_mat, 0)
    distance = calcTour.fc(dis_mat, path)
