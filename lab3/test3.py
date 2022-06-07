from GA import GeneticAlgorithm
import readData
import time

tsp_files = ['berlin52.tsp', 'ch150.tsp', 'gr48.tsp', 'pr107.tsp']
atsp_files = ['ftv70.atsp', 'br17.atsp', 'ft53.atsp', 'ftv170.atsp']
mutation = [0, 0.005, 0.01, 0.02, 0.05, 0.1]
# for i in tsp_files:
#     instance = readData.ReadData('../lab1/TSP_Data/' + i)
#     for j in mutation:
#         with open(f'wyniki3/{i}{j}','w') as data:
#             for _ in range(5):
#                 a = time.time()
#                 ga = GeneticAlgorithm(10000,3,instance,0.5,1,True,MUTATION_CHANCE=j)
#                 imp = ga.simulate()
#                 diff = time.time() - a
#                 best_gen = ga.GetGenBest()
#                 data.write(str(diff))
#                 data.write('; ')
#                 for z in best_gen:
#                     data.write(str(z))
#                     data.write('; ')
#                 data.write('\n')
#                 best_gen.clear()

for i in atsp_files:

    instance = readData.ReadData('../lab1/TSP_Data/' + i,True)
    for j in mutation:
        with open(f'wyniki3/{i}{j}','w') as data:
            for _ in range(5):
                a = time.time()
                ga = GeneticAlgorithm(10000,3,instance,0.5,1,False,MUTATION_CHANCE=j)
                imp = ga.simulate()
                diff = time.time() - a
                best_gen = ga.GetGenBest()
                data.write(str(diff))
                data.write('; ')
                for z in best_gen:
                    data.write(str(z))
                    data.write('; ')
                data.write('\n')
                best_gen.clear()
