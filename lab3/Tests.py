
from GA import GeneticAlgorithm
import readData
import time
from scipy.stats import wilcoxon

tsp_files = ['berlin52.tsp', 'ch150.tsp', 'gr48.tsp', 'pr107.tsp']
atsp_files = ['ftv70.atsp', 'br17.atsp', 'ft53.atsp', 'ftv170.atsp']



islands = [1,2,3,4,5,6]

#znajdź najlepszą wartość dla danej generacji
def getValueAt(gen,Improvements):
    ix = -1
    while ix+1 < len(Improvements):
        mb = Improvements[ix+1]
        if mb[0]>gen:
            break
        ix += 1
        
    return Improvements[ix][1]

def getFinal(Improvements):
    return Improvements[-1][1]

#Test wysp
def test2():
    REPEATS = 5
    rng = range(1,5002,250)

    for f in tsp_files:
        instance = readData.ReadData('../lab2/TSP_Data/'+ f)
        avgSums = [[] for _ in range(len(islands))]
        with open(f"t2_{f}",'w') as data:
            data.write("ISLANDS;")
            for gwas in rng:
                data.write(str(gwas))
                data.write(";")
            data.write("\n")
            for i in range(len(islands)):

                avgSums[i] = [0 for _ in range(len(rng))]

                print(f"Starting sims for {f}, islands={islands[i]}")
                for j in range(REPEATS):
                    ga = GeneticAlgorithm(int(5002/islands[i]),islands[i],instance,0.25,4,True,ratio=1.0)
                    res = ga.simulate()

                    kix = 0
                    for k in rng:
                        val = getValueAt(int(k/islands[i]),res)
                        avgSums[i][kix] += val
                        kix+=1


                for v in range(len(avgSums[i])):
                    avgSums[i][v] = avgSums[i][v]/REPEATS
                data.write(str(islands[i]))
                data.write(";")
                for a in avgSums[i]:
                    data.write(str(a))
                    data.write(";")
                data.write("\n")

#test wieku
def test5():
    REPEATS = 10
    rng = range(10,51,10)
    with open(f"test5",'w') as data:
        data.write("inst;")
        for awfin in rng:
            data.write(str(awfin))
            data.write(";")
        data.write("\n")

        for f in tsp_files:
            instance = readData.ReadData('../lab2/TSP_Data/'+ f)
    
            avgSums = [0 for _ in range(len(rng))]
            kix=0
            for life in rng:
                print(f"Starting sims for {f}, life={life}")
                
                for j in range(REPEATS):
                    ga = GeneticAlgorithm(5000,1,instance,1.0,4,True,ratio=0.9,LIFE_EXPECTANCY=life)
                    res = ga.simulate()

                    val = getFinal(res)
                    print(f"val: {val}")
                    avgSums[kix] += val
                kix+=1
            
            for v in range(len(avgSums)):
                avgSums[v] = avgSums[v]/REPEATS

            data.write(f)
            data.write(";")
            for a in avgSums:
                data.write(str(a))
                data.write(";")
            data.write("\n")

#mierzenie czasu działania
tc_files = ['gr24.tsp','gr48.tsp','berlin52.tsp','pr107.tsp','gr120.tsp','ch150.tsp']
tc_files2 = ['st70.tsp','pr264.tsp','lin318.tsp']
tc_files3 = ['ts225.tsp']
tc_files4 = ['p654.tsp']

def testTC():
    REPEATS = 10
    with open(f"testTC4",'w') as data:

        for f in tc_files4:
            print(f"Starting sims for {f}")
            instance = readData.ReadData('../lab1/TSP_Data/'+ f)
            times = []

            for j in range(REPEATS):
                start = time.time()
                ga = GeneticAlgorithm(2000,1,instance,0.5,4,True,ratio=0.9)
                ga.simulate()
                diff = time.time() - start
                print(diff)
                times.append(diff)
            
            data.write(str(f))
            data.write(";")

            for t in times:
                data.write(str(t))
                data.write(";")
            
            data.write("\n")
#test2()
mig_files = ['berlin52.tsp']
def testMIG():
    REPEATS = 50
    with open(f"testNOEXT",'w') as data:

        for f in mig_files:
            print(f"Starting sims for {f}")
            instance = readData.ReadData('../lab1/TSP_Data/'+ f)
            results = []

            for j in range(REPEATS):
                ga = GeneticAlgorithm(5000,3,instance,0.5,4,True,ratio=1.0)
                res = ga.simulate()
                print(getFinal(res))
                results.append(getFinal(res))
            
            data.write(str(f))
            data.write(";")

            for t in results:
                data.write(str(t))
                data.write(";")
            
            data.write("\n")

def testWil(d1,d2):
    with open(d1) as f1:
        for l in f1:
            data1 = l.strip().split(";")
    with open(d2) as f2:
        for l in f2:
            data2 = l.strip().split(";")

    data1.pop(0)
    data1.pop(-1)
    data2.pop(0)
    data2.pop(-1)

    for i in range(len(data1)):
        data1[i] = int(data1[i])
        data2[i] = int(data2[i])

    w,p = wilcoxon(data1,data2)
    print(w,p)

#testWil('testNOEXT','testEXT')
