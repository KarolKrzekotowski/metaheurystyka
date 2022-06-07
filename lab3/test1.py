from GA import GeneticAlgorithm
import readData
import time

tsp_files = ['berlin52.tsp', 'ch150.tsp', 'gr48.tsp', 'pr107.tsp']
atsp_files = ['ftv70.atsp', 'br17.atsp', 'ft53.atsp', 'ftv170.atsp']

methods = {
    'ox': 1,
    'spx': 3,
    'cx': 4
}
# generations, islandNb, instance,r_cross,xmode,useInvert
# POP: 20, NC: 0.002, NA: 0.75 MigC: 0.01, MM: (PopS/10), ParS: (PopS/2), Eli: (PopS/15), MutC: 0.01, LEx: 50

# CZAS {250,500...10000} generacja i najlepszy do tej generacji


# for i in tsp_files:
#     instance = readData.ReadData('../lab1/TSP_Data/'+ i)
#     for j in methods:
#         with open(f'{j}{i}','w') as data:
#             for _ in range(5):
#                 a = time.time()
#                 ga = GeneticAlgorithm(10000,3,instance,0.5,methods[j],True)
#
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



#
for i in atsp_files:
    instance = readData.ReadData('../lab1/TSP_Data/'+ i,True)
    for j in methods:
        with open(f'{j}{i}','w') as data:
            for _ in range(5):
                a = time.time()
                ga = GeneticAlgorithm(10000,3,instance,0.5,methods[j],False)

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

