import copy
import random
import time

import krandom
import nearestNeighbour
import readData
import calcTour
import displayTour
import tsplib95
import  generateData
import nearestNeigbor2
import Opt2


# pliki berlin52.tsp gr120.tsp d198.tsp ch150.tsp
# k - zakres k: 1-100
# czas
# PRD
# 'br17.atsp', 'ft53.atsp

# pliki = [ 'berlin52.tsp', 'ch150.tsp','gr120.tsp', 'pcb442.tsp' ]
# pliki = ['br17.atsp', 'ft53.atsp', 'ftv170.atsp','rbg323.atsp']
# for file in pliki:
#     # instance = readData.ReadData('TSP_Data/'+file)
#     # size = instance.size
#     # dis_mat = instance.GetDistanceMat()
#     # bestpath = displayTour.loadPath(f'TSP_Data/{file.replace(".tsp","")}.opt.tour')
#     # bestdistance = calcTour.fc(dis_mat,bestpath)
#     problem1 = tsplib95.load_problem('TSP_Data/'+ file)
#     dimension = len(list(problem1.get_nodes()))
#     size = dimension
#     edges = list(problem1.get_edges())
#
#     mat = [[None for _ in range(dimension)] for _ in range(dimension)]
#
#     for edge in edges:
#         mat[edge[0] - 1][edge[1] - 1] = problem1.get_weight(*edge)
#     dis_mat = copy.copy(mat)
#
#     if file == 'rbg323.atsp':
#         bestdistance = 1326
#     if file == 'ftv170.atsp':
#         bestdistance = 2755
#     elif file == 'br17.atsp':
#         bestdistance = 39
#     elif file == 'ft53.atsp':
#         bestdistance = 6905
#     with open('Wyniki3/' + file + 'wyniki.csv', 'w') as data:
#         data.write(str(size)+'; '+ 'czaskrandom; prdrandom; czas nn; prdNN\n')
#         for k in range(1, 101):
#             time1 = time.time()
#             path1 = krandom.krandom(size,dis_mat)
#
#             time2 = time.time()
#             timediff1 = time2 - time1
#             print("--------------------")
#             time1 = time.time()
#             path2,dystans2  = nearestNeighbour.run(size,dis_mat,random.randint(0,size-1))
#             time2 = time.time()
#             print(k)
#             timediff2 = time2 - time1
#             dystans1 = calcTour.fc(dis_mat, path1)
#             prd1 = calcTour.PRD(dystans1,bestdistance)
#             prd2 = calcTour.PRD(dystans2, bestdistance)
#             data.write(str(size) +'; '+ str(timediff1) +'; '+ str(prd1) + '; '+ str(timediff2) +'; '+ str(prd2)+ '\n')




dimension = [30,70,120,200]
minimum = [10,20,30,40]
maximum = [100,150,250,300]
seed = [13,19,8,29]
option = "FULL_MATRIX"
for i in range(len(dimension)):

    generateData.generateData(dimension[i], seed[i], option, minimum[i], maximum[i])
    file = 'TSP_Data/random_instance_file.atsp'
    instance = readData.ReadData(file)
    size = instance.size
    dis_mat = instance.GetDistanceMat()
    # #gdybanie nad najlepszym wynikiem
    bestpath = nearestNeigbor2.run(size, dis_mat)
    bestpath = Opt2.Opt2(instance, bestpath)
    bestdistance = calcTour.fc(dis_mat, bestpath)
    # #koniec gdybania
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []

    for k in range(1, 101):
        time1 = time.time()
        path1 = krandom.krandom(size,dis_mat)

        time2 = time.time()
        timediff1 = time2 - time1
        print("--------------------")
        time1 = time.time()
        path2,dystans2 = nearestNeighbour.run(size,dis_mat,random.randint(0,size-1))
        time2 = time.time()
        print(k)
        timediff2 = time2 - time1
        dystans1 = calcTour.fc(dis_mat, path1)
        list1.append(str(size) )
        list2.append(dystans1)
        list3.append(str(timediff1))
        list4.append(dystans2)
        list5.append(str(timediff2))

    with open('Wyniki3/' + file.replace('TSP_Data/', "") + str(i) + 'wyniki.csv', 'w') as data:
        for i in range(len(list1)):

            prd1 = calcTour.PRD(list2[i], bestdistance)
            prd2 = calcTour.PRD(list4[i], bestdistance)
            data.write(str(size) +'; '+ str(timediff1) +'; '+ str(prd1) + '; '+ str(timediff2) +'; '+ str(prd2)+ '\n')