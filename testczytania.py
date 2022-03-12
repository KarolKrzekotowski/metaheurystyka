import time

start_time = time.time()
import sys
from readData import ReadData



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


if len(sys.argv) < 2:
    print("need inpute file")
    sys.exit(1)
t = testczytania(sys.argv[1])
t._write_info()
