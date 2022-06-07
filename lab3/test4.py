from GA import GeneticAlgorithm
import readData
import time
from statistics import mean



tsp_files = ['berlin52.tsp', 'ch150.tsp', 'gr48.tsp', 'pr107.tsp']
atsp_files = ['ftv70.atsp', 'br17.atsp', 'ft53.atsp', 'ftv170.atsp']
ratio = [
0.0,
0.1,
0.2,
0.3,
0.4,
0.5,
0.6,
0.7,
0.8,
0.9,
1.0,
]
results = []
for i in tsp_files:
    instance = readData.ReadData('../lab1/TSP_Data/' + i)
    with open(f'wyniki4/{i}', 'w') as data:
        for j in ratio:

            for _ in range(10):

                ga = GeneticAlgorithm(10000,3,instance,0.5,1,True,ratio=j)
                imp = ga.simulate()
                results.append(imp[-1][1])

            minimum = min(results)
            maximum = max(results)
            avg = mean(results)
            data.write(str(minimum)+'; '+str(maximum)+';'+str(avg)+'\n')
            results.clear()
# for i in atsp_files:
#     instance = readData.ReadData('../lab1/TSP_Data/' + i,True)
#     with open(f'wyniki4/{i}', 'w') as data:
#         for j in ratio:
#
#             for _ in range(10):
#
#                 ga = GeneticAlgorithm(10000,3,instance,0.5,1,False,ratio=j)
#                 imp = ga.simulate()
#                 results.append(imp[-1][1])
#
#             minimum = min(results)
#             maximum = max(results)
#             avg = mean(results)
#             data.write(str(minimum)+'; '+str(maximum)+';'+str(avg)+'\n')
#             results.clear()

