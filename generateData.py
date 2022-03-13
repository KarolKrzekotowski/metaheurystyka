import random
import sys
from scipy.spatial.distance import pdist, squareform
import numpy as np
class generateData():
    # Argumentem
    # funkcji
    # powinien
    # być
    # rozmiar problemu,
    # ziarno generatora liczbpseudolosywch,
    # wariant problemu
    # zakresie# wartości.

    def __init__(self, dimension, seed, option, minimum, maximum):
        self.dimension = dimension
        self.seed = seed
        self.option = option
        self.min = minimum
        self.max = maximum
        self.xlist = []
        self.ylist = []
        self.inf = False
        self.genEuc2d()
        if self.option == "EUC_2D":
            self.genFileEuc2d()
        elif self.option == "LOWER_DIAG_ROW":
            self.Distance = self.genDistance()
            self.genFileLower()
        elif self.option == "FULL_MATRIX":
            self.inf = True
            self.Distance = self.genDistance()
            self.genFileMatrix()

    def genEuc2d(self):
        random.seed(self.seed)
        list1 = []
        list2 = []
        loops = 0
        count = 0
        while loops < self.dimension:

            x = float(random.randint(self.min, self.max))
            y = float(random.randint(self.min, self.max))


            indexes = [i for i, j in enumerate(list1) if j == x]
            indexes2 = [i for i, j in enumerate(list2) if j == y]
            for j in indexes:
                if list2[j] != y:
                    count += 1

            if count == len(indexes2):
                list1.append(x)
                list2.append(y)
                loops += 1
            count = 0
        self.xlist = list1
        self.ylist = list2


    def genFileEuc2d(self):

        xlist = self.xlist
        ylist = self.ylist
        info2 = ''
        info = 'NAME: random_instance_file\n' \
                'TYPE: TSP\n' \
                'COMMENT: comment\n' \
                'DIMENSION: ' + str(self.dimension) +'\n' \
                'EDGE_WEIGHT_TYPE: EUC_2D\n' \
                'NODE_COORD_SECTION\n'
        for i in range(0, len(xlist)):
            info2 += "{} {} {}\n".format(i+1, xlist[i], ylist[i])
        with open(f'TSP_Data/random_instance_file.tsp', 'w') as data:
            data.write(info + info2 + "EOF\n")
        data.close()

    def genFileLower(self):

        Distance = self.Distance
        matrix = '0 '
        for i in range(1, self.dimension):
            for j in range(0, i+1):
                matrix += str(Distance[i][j]) +' \n'

        info = 'NAME: random_instance_file\n' \
               'TYPE: TSP\n' \
               'COMMENT: COMMENT\n' \
               'DIMENSION: ' + str(self.dimension) +'\n' \
               'EDGE_WEIGHT_TYPE: EXPLICIT\n' \
               'EDGE_WEIGHT_FORMAT: LOWER_DIAG_ROW \n' \
               'DISPLAY_DATA_TYPE: TWOD_DISPLAY \n' \
               'EDGE_WEIGHT_SECTION\n' \
                + matrix
        with open(f'TSP_Data/random_instance_file.tsp', 'w') as data:
            data.write(info + "EOF\n")
        data.close()


    def genDistance(self):
        cities = []
        for i in range(len(self.xlist)):
            cities.append(np.array([self.xlist[i], self.ylist[i]]))

        DistanceMat = np.round(squareform(pdist(cities)))
        return DistanceMat

    def genFileMatrix(self):
        Distance = self.Distance.astype(float)
        print(Distance)
        matrix = ''
        val = float(0.0)

        for i in range(0, self.dimension):
            for j in range(0, self.dimension):
                if j == 2 :
                    matrix += '\n'
                if Distance[i][j].item() == val:
                    Distance[i,j] = 99999

                matrix += str(Distance[i][j])+ ' '
            matrix += '\n'
        info = 'NAME: name\n' \
               'TYPE: ATSP\n' \
               'COMMENT: comment\n' \
               'DIMENSION: ' + str(self.dimension) + '\n' \
               'EDGE_WEIGHT_TYPE: EXPLICIT\n' \
               'EDGE_WEIGHT_FORMAT: FULL_MATRIX\n' \
               'EDGE_WEIGHT_SECTION\n' + str(matrix)




        # DIMENSION: 17
        # EDGE_WEIGHT_TYPE: EXPLICIT
        # EDGE_WEIGHT_FORMAT: FULL_MATRIX
        # EDGE_WEIGHT_SECTION

        with open(f'TSP_Data/random_instance_file.atsp', 'w') as data:
            data.write(info + "EOF\n")
        data.close()


generateData(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]))







