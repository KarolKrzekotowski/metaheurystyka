import random
import sys
import nearestNeighbour
import krandom
import Opt2
import calcTour
import time
import generateData
import readData
from scipy.stats import wilcoxon
import displayTour


def test4():
    minimum = 50
    maximum = 200
    #powtórzenia krandom dla danej macierzy
    repeats = 50
    #ilość macierzy dla danego rozmiaru
    matrixrepeats = 10
    option = "FULL_MATRIX"
    file = 'TSP_Data/random_instance_file.atsp'
    print("---- TEST 2OPT NN vs krandom init ----")
    #rozmiary grafów:
    for dim in range(20,70,10):
        print(f"---- Tests for dim={dim} -----")
        #uśrednione wyniki dla danej macierzy (1 z matrixrepeats)
        avgNNRes = []
        avgKRRes = []
        avgNNTime = []
        avgKRTime = []
        for i in range(0,matrixrepeats):
            print(f"- matrix {i+1}/{matrixrepeats} -")
            #wygeneruj i załaduj instancję
            generateData.generateData(dim,random.randint(0,sys.maxsize),option,minimum,maximum)
            instance = readData.ReadData(file)
            size = instance.size
            matrix = instance.GetDistanceMat()

            NNRes2Opt = []
            NNTime2Opt = []
            #2OPT+NN dla każdego pkt początkowego
            for pt in range(0,size):
                t1 = time.time()
                path,_ = nearestNeighbour.run(size,matrix,pt)
                path = Opt2.Opt2(instance,path)

                t2 = time.time()
                NNRes2Opt.append(calcTour.fc(matrix,path))
                NNTime2Opt.append(t2-t1)

            KRRes2Opt = []
            KRTime2Opt = []
            #2OPT+NN dla losowych permutacji
            for pt in range(0,repeats):
                t1 = time.time()
                path = krandom.krandom(size,matrix,k=1)
                path = Opt2.Opt2(instance,path)
                t2 = time.time()
                KRRes2Opt.append(calcTour.fc(matrix,path))
                KRTime2Opt.append(t2-t1)

            krmin = min(KRRes2Opt)
            nnmin = min(NNRes2Opt)
            ref = min(krmin,nnmin)
            
            print(f"[NN]: {nnmin}, [kr]: {krmin}")

            NNprd = 0.0
            KRprd = 0.0
            for j in range(0,size):
                NNprd += calcTour.PRD(NNRes2Opt[j],ref)
            for j in range(0,repeats):
                KRprd += calcTour.PRD(KRRes2Opt[j],ref)

            avgNNRes.append(NNprd/size)
            avgKRRes.append(KRprd/repeats)
            avgNNTime.append(sum(NNTime2Opt)/size)
            avgKRTime.append(sum(KRTime2Opt)/repeats)
        print(avgNNRes)
        print(avgNNTime)
        print(avgKRRes)
        print(avgKRTime)
        with open('Wyniki4/'+str(dim)+f".{option}.wyniki.csv",'w') as data:
            data.write("NNprd;NNtime;KRprd;KRtime\n")
            for k in range(0,matrixrepeats):
                data.write(str(avgNNRes[k])+';'+str(avgNNTime[k])+';'+str(avgKRRes[k])+';'+str(avgKRTime[k])+'\n')

def test6():
    minimum = 50
    maximum = 200
    #ilość macierzy na rozmiar
    matrixrepeats = 100

    option = "LOWER_DIAG_ROW"
    file = 'TSP_Data/random_instance_file.tsp'
    print("---- TEST NN rozproszenie ----")
    dims = []
    dimPerMin = []
    dimPerMax = []
    for dim in range(10,85,5):
        print(f"---- Tests for dim={dim} -----")
        dims.append(dim)
        rmin = []
        rmax = []
        for i in range(0,matrixrepeats):
            generateData.generateData(dim,random.randint(0,sys.maxsize),option,minimum,maximum)
            instance = readData.ReadData(file)
            size = instance.size
            matrix = instance.GetDistanceMat()

            res = []
            #uzyskaj wszystkie NN z możliwych
            for pt in range(0,dim):
                path,_ = nearestNeighbour.run(size,matrix,pt)
                res.append(calcTour.fc(matrix,path))

            #wyniki dla danej macierzy
            NNmin = min(res)
            NNmax = max(res)
            NNavg = sum(res)/dim
            
            rmin.append(NNmin/NNavg)
            rmax.append(NNmax/NNavg)

        dimPerMin.append(sum(rmin)/matrixrepeats)
        dimPerMax.append(sum(rmax)/matrixrepeats)
    
    with open('Wyniki6/'+f"{option}.wyniki.csv",'w') as data:
        for ඞ in range(len(dims)):
            data.write(f"{str(dims[ඞ])};{str(dimPerMin[ඞ])};{str(dimPerMax[ඞ])}"+"\n")

def testWil():
    minimum = 50
    maximum = 200
    #powtórzenia dla danej macierzy
    repeats = 10
    #ilość macierzy dla danego rozmiaru
    matrixrepeats = 20
    option = "EUC_2D"
    file = 'TSP_Data/random_instance_file.tsp'
    print("---- TEST Wilcoxon best case scenario ----")
    NNRes = []
    KRRes = []
    #rozmiary grafów:
    for dim in range(30,60,10):
        print(f"---- Tests for dim={dim} -----")
        #uśrednione wyniki dla danej macierzy (1 z matrixrepeats)
        
        for i in range(0,matrixrepeats):
            print(f"- matrix {i+1}/{matrixrepeats} -")
            #wygeneruj i załaduj instancję
            generateData.generateData(dim,random.randint(0,sys.maxsize),option,minimum,maximum)
            instance = readData.ReadData(file)
            size = instance.size
            matrix = instance.GetDistanceMat()

            NNRes2Opt = []
            #2OPT+NN dla każdego pkt początkowego
            for pt in range(0,repeats):
                path,_ = nearestNeighbour.run(size,matrix,random.randint(0,size-1))
                path = Opt2.Opt2(instance,path)
                NNRes2Opt.append(calcTour.fc(matrix,path))

            KRRes2Opt = []
            #2OPT+NN dla losowych permutacji
            for pt in range(0,repeats):
                path = krandom.krandom(size,matrix,k=1)
                path = Opt2.Opt2(instance,path)
                KRRes2Opt.append(calcTour.fc(matrix,path))

            krmin = min(KRRes2Opt)
            nnmin = min(NNRes2Opt)
            
            print(f"[NN]: {nnmin}, [kr]: {krmin}")
            NNRes.append(nnmin)
            KRRes.append(krmin)

    w,p = wilcoxon(NNRes,KRRes)
    print(w,p)
    print(NNRes)
    print(KRRes)

            
    
        
#test6()
#test4()
testWil()

