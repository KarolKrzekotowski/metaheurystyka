import tsplib95
import numpy as np
import copy
import sys
#sys.path.insert()
import readData
import Neighborhood
import nearestNeigbor2
from Paths import fc, invert, swap

#neighbouring function


class TabuSearch:

    def __init__(self, bestdistance, path, dis_mat):
        self.path = path
        self.bestdistance = bestdistance
        self.dis_mat = dis_mat
        self.NH = Neighborhood.Neighborhood(len(self.path))

    def run(self, max_iterations, maxTabuSize, type=invert):
        sBest = copy.copy(self.path)

        bestCandidate = []
        bestCandidatePath = copy.copy(self.path)
        bestCandidateFC = fc(self.dis_mat,bestCandidatePath)
        print(fc(self.dis_mat,bestCandidatePath))
        tabuList = []
        tabuListPerm = []
        tabuList.append(sBest)
        x = 0
        while x < max_iterations:
            sNeighborhood = self.NH.get()

            bestCandidate = sNeighborhood[0]
            for sCandidate in sNeighborhood:
                if sCandidate not in tabuListPerm:
                    sCandidatePath = invert(bestCandidatePath,sCandidate)
                    sCandidateFC = fc(self.dis_mat,sCandidatePath)
                    if (sCandidateFC < bestCandidateFC):
                        bestCandidatePath = sCandidatePath
                        bestCandidate = sCandidate
                        bestCandidateFC = sCandidateFC
    
            if fc(self.dis_mat,bestCandidatePath) < fc(self.dis_mat,sBest):
                sBest = bestCandidatePath
                print(tabuListPerm)
                print("best of", x, ":", fc(self.dis_mat, sBest))

            tabuListPerm.append(bestCandidate)

            x += 1
            if (len(tabuListPerm) > maxTabuSize):
                tabuListPerm.pop(0)

        print(fc(self.dis_mat,sBest))





types = {
    'swap': swap,
    'invert': invert
}

if __name__ == '__main__':
    file = sys.argv[1]
    instance = readData.ReadData(file)
    size = instance.size
    dis_mat = instance.GetDistanceMat()
    path = nearestNeigbor2.run(size, dis_mat, 0)
    distance = fc(dis_mat, path)
    halo = TabuSearch(distance,path,dis_mat)
    type = sys.argv[4]
    if type in types:
        func = types[type]
        halo.run(int(sys.argv[2]),int(sys.argv[3]),func)
    # halo.run(int(sys.argv[2]))
