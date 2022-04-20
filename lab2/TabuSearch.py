import tsplib95
import numpy as np
import copy
import sys
#sys.path.insert()
import readData
import Neighborhood
import nearestNeigbor2
from Paths import fc, invert

#neighbouring function


class TabuSearch:

    def __init__(self, bestdistance, path, dis_mat):
        self.path = path
        self.bestdistance = bestdistance
        self.dis_mat = dis_mat
        self.NH = Neighborhood.Neighborhood(len(self.path))

    def run(self, max_iterations):
        sBest = copy.copy(self.path)
        bestCandidate = copy.copy(self.path)
        print(fc(self.dis_mat,bestCandidate))
        tabuList = []
        tabuList.append(sBest)
        x = 0
        while x < max_iterations:
            sNeighborhood = self.NH.get(bestCandidate,invert)
            bestCandidate = sNeighborhood[0]
            for sCandidate in sNeighborhood:
                if  sCandidate not in tabuList and fc(self.dis_mat, sCandidate) < fc(self.dis_mat, bestCandidate):
                    bestCandidate = sCandidate
            if fc(self.dis_mat,bestCandidate) < fc(self.dis_mat,sBest):
                sBest = bestCandidate
            tabuList.append(bestCandidate)
            print("best of",x,":",fc(self.dis_mat,sBest))
            x += 1
        print(fc(self.dis_mat,sBest))







if __name__ == '__main__':
    file = sys.argv[1]
    instance = readData.ReadData(file)
    size = instance.size
    dis_mat = instance.GetDistanceMat()
    path = nearestNeigbor2.run(size, dis_mat, 0)
    distance = fc(dis_mat, path)
    halo = TabuSearch(distance,path,dis_mat)
    halo.run(100)
