import imp
import time

start_time = time.time()
import sys
from readData import ReadData
import displayTour
import calcTour

class testczytania():

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
        print(self.dis_mat,"dismat")

        #test cykli
        bestpath = displayTour.loadPath(f'TSP_Data/{self.instance.name}.opt.tour')

        if bestpath != None:
            displayTour.printPath(self.dis_mat,bestpath)
            print("rozwiązanie: ",calcTour.fc(self.dis_mat,bestpath))
            displayTour.EUCgraph(self.instance,bestpath)

if len(sys.argv) < 2:
    print("need inpute file")
    sys.exit(1)
t = testczytania(sys.argv[1])
t._write_info()
