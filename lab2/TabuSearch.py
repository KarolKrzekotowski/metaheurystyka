import tsplib95
import lab1.TSP.readData as readData
import lab1.TSP.nearestNeigbor2 as KNN
import lab1.TSP.calcTour as calcTour
import numpy as np
import copy
import  sys
np.concatenate

#neighbouring function


class TabuSearch:

    def __init__(self, bestdistance, path, dis_mat):
        self.path = path
        self.bestdistance = bestdistance
        self.dis_mat = dis_mat

    def run(self, max_iterations):
        sBest = copy.copy(self.path)
        bestCandidate = copy.copy(self.path)
        tabuList = []
        tabuList.append(sBest)
        x = 0
        while x < max_iterations:
            sNeighborhood = getNeighbors(bestCandidate)
            bestCandidate = sNeighborhood[0]
            for sCandidate in sNeighborhood:
                if  sCandidate not in tabuList and calcTour.fc(self.dis_mat, sCandidate) > calcTour.fc(self.dis_mat, bestCandidate):
                    bestCandidate = sCandidate
            if calcTour.fc(self.dis_mat,bestCandidate) > calcTour.fc(sBest):
                sBest = bestCandidate
            tabuList.append(bestCandidate)







if __name__ == '__main__':
    file = sys.argv[1]
    instance = readData.ReadData(file)
    size = instance.size
    dis_mat = instance.GetDistanceMat()
    path = KNN.run(size, dis_mat, 0)
    distance = calcTour.fc(dis_mat, path)
