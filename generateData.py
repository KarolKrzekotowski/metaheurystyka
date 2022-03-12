import random
import sys

import numpy
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
        if self.option == "EUC_2D":
            self.genEuc2d()
            self.genFileEuc2d()
        elif self.option == "LOWER_DIAG_ROW":
            self.genLower()
            self.genFileLower()

    def genEuc2d(self):
        random.seed(self.seed)
        list1 = []
        list2 = []
        loops = 0
        count = 0
        while loops < self.dimension:

            x = float(random.randint(self.min, self.max))
            y = float(random.randint(self.min, self.max))

            print(x,y,loops)
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

    def genLower(self):
        pass


    def genFileLower(self):
        pass


generateData(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]))







