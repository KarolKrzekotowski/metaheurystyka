
import time

start_time = time.time()
import sys
from scipy.spatial.distance import pdist, squareform
import numpy as np
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)

class ReadData():
    def __init__(self, filename):
        self.atsp = False
        self.sufix = ".tsp"
        self.filename = filename
        self.name = filename[:-4]
        self.size = self.getSize()
        self.EdgeWeightType = self.getEdgeWeightType()
        self.format_ = self.getFormat()  # for EXPLICIT data only
        self.time_to_read = 0


    def getFormat(self):
        format = "None"
        try:
            with open(f'TSP_Data/{self.name}{self.sufix}') as data:
                datalist = data.read().split()
                for ind, elem in enumerate(datalist):
                    if elem == "EDGE_WEIGHT_FORMAT:":
                        format = datalist[ind + 1]
                        break
                    elif elem == "EDGE_WEIGHT_FORMAT":
                        format = datalist[ind + 2]
                        break
            return format

        except :
            try:
                self.name = self.filename[:-5]
                with open(f'TSP_Data/{self.name}{self.sufix}') as data:

                    datalist = data.read().split()
                    for ind, elem in enumerate(datalist):
                        if elem == "EDGE_WEIGHT_FORMAT:":
                            format = datalist[ind + 1]
                            break
                        elif elem == "EDGE_WEIGHT_FORMAT":
                            format = datalist[ind + 2]
                            break

                    return format
            except:
                print("wrong input data")
                sys.exit(1)

    def getEdgeWeightType(self):
        EdgeType = "None"
        try:
            with open(f'TSP_Data/{self.name}{self.sufix}') as data:
                datalist = data.read().split()
                for ind, elem in enumerate(datalist):
                    if elem == "EDGE_WEIGHT_TYPE:":
                        EdgeType = datalist[ind + 1]
                        # print(EdgeType)
                        break
                    elif elem == "EDGE_WEIGHT_TYPE":
                        EdgeType = datalist[ind + 2]
                        # print(EdgeType)
                        break
            return EdgeType
        except:
            try:
                self.name = self.filename[:-5]
                with open(f'TSP_Data/{self.name}{self.sufix}') as data:
                    datalist = data.read().split()
                    for ind, elem in enumerate(datalist):
                        if elem == "EDGE_WEIGHT_TYPE:":
                            EdgeType = datalist[ind + 1]
                            # print(EdgeType)
                            break
                        elif elem == "EDGE_WEIGHT_TYPE":
                            EdgeType = datalist[ind + 2]
                            # print(EdgeType)
                            break
                return EdgeType
            except:
                print("wrong input file")
                sys.exit(1)



    def getSize(self):
        """
        Return size of instances (i.e. Number of
        cities)

        """
        size = 0
        try:

            with open(f'TSP_Data/{self.name}{self.sufix}') as data:
                datalist = data.read().split()
                for ind, elem in enumerate(datalist):
                    if elem == "DIMENSION:":
                        size = datalist[ind + 1]
                        # print(size)
                        break
                    elif elem == "DIMENSION":
                        size = datalist[ind + 2]
                        # print(size)
                        break
            return int(size)
        except IOError:
            try:
                self.name = self.filename[:-5]
                self.sufix =".atsp"
                with open(f'TSP_Data/{self.name}{self.sufix}') as data:

                    datalist = data.read().split()

                    for ind, elem in enumerate(datalist):
                        if elem == "DIMENSION:":
                            size = datalist[ind + 1]
                            break
                        elif elem == "DIMENSION":
                            size = datalist[ind + 2]
                            break

                return int(size)
            except:
                print("file not found1")
                sys.exit(1)


    def read_Data(self):
        with open(f'TSP_Data/{self.name}{self.sufix}') as data:
            cities = []
            Isdata = True
            while (Isdata):
                line = data.readline().split()
                if len(line) <= 0:
                    break
                tempcity = []
                for i, elem in enumerate(line):
                    try:
                        temp = float(elem)
                        tempcity.append(temp)
                    except ValueError:
                        break
                if len(tempcity) > 0:


                    line = data.readline().split()
                    for i, elem in enumerate(line):
                        try:
                            temp = float(elem)
                            tempcity.append(temp)
                        except ValueError:
                            break
                    if len(tempcity) > 0:
                        cities.append(np.array(tempcity))



        return np.array(cities)

    def GetDistanceMat(self):
        if self.EdgeWeightType == "EXPLICIT":
            DistanceMat = self.getMat()
            self.time_to_read = time.time() - start_time
            return DistanceMat
        elif self.EdgeWeightType == "EUC_2D":
            DistanceMat = self.EuclidDist()
            self.time_to_read = time.time() - start_time
            return DistanceMat

        else:
            return None

    def EuclidDist(self):
        cities = self.read_Data()
        # DistanceDict = {}
        A = cities[:, 1:3]
        DistanceMat = np.round(squareform(pdist(A)))
        return DistanceMat


    def getMat(self):
        DataFormat = self.getFormat()
        if DataFormat == "FULL_MATRIX":
            cities = self.read_Data()
            DistanceMat = cities[:self.size]
            print("ez")
            return DistanceMat

        elif DataFormat == "LOWER_DIAG_ROW":
            with open(f'TSP_Data/{self.name}{self.sufix}') as file:
                indicator = False
                data = file.read().split()
                templist = []
                cities = []
                for elem in data:
                    if elem == "EDGE_WEIGHT_SECTION":
                        indicator = True
                        continue
                    if indicator:
                        try:
                            it = float(elem)
                            templist.append(it)
                        except:
                            break
                        if it == 0:
                            cities.append(templist)
                            templist = []
                DistanceMat = np.zeros((self.size, self.size))
                for i in range(self.size):
                    temp = []
                    l = len(cities[i])
                    for j in range(self.size):
                        if j <= (l - 1):
                            temp.append(cities[i][j])
                        else:
                            temp.append(cities[j][i])
                    DistanceMat[i] = temp
                return DistanceMat

        else:
            sys.exit("No Format Match for EXPLICIT data")
