import copy
import time

import krandom
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

pliki = [  'pcb442.tsp' ]
for file in pliki:
    instance = readData.ReadData('TSP_Data/'+file)
    size = instance.size
    dis_mat = instance.GetDistanceMat()
    bestpath = displayTour.loadPath(f'TSP_Data/{file.replace(".tsp","")}.opt.tour')
    bestdistance = calcTour.fc(dis_mat,bestpath)
    # problem1 = tsplib95.load_problem('TSP_Data/'+ file)
    # dimension = len(list(problem1.get_nodes()))
    # size = dimension
    # edges = list(problem1.get_edges())
    #
    # mat = [[None for _ in range(dimension)] for _ in range(dimension)]
    #
    # for edge in edges:
    #     mat[edge[0] - 1][edge[1] - 1] = problem1.get_weight(*edge)
    # dis_mat = copy.copy(mat)

    if file == 'rbg323.atsp':
        bestdistance = 1326
    if file == 'ftv170.atsp':
        bestdistance = 2755
    elif file == 'br17.atsp':
        bestdistance = 39
    elif file == 'ft53.atsp':
        bestdistance = 6905
    with open('Wyniki2/' + file + 'wyniki.csv', 'w') as data:
        for k in range(1, 101):


            print("--------------------")

            time1 = time.time()

            path = nearestNeigbor2.run(size, dis_mat, k)
            print(k)

            time2 = time.time()
            timediff = time2 - time1
            dystans = calcTour.fc(dis_mat, path)
            prd = calcTour.PRD(dystans,bestdistance)
            data.write(str(k) +'; '+ str(prd) + '; '+ str(timediff) +'\n')




# dimension = [30,70,120,200]
# minimum = [10,20,30,40]
# maximum = [100,150,250,300]
# seed = [13,19,8,29]
# option = "LOWER_DIAG_ROW"
# for i in range(len(dimension)):
#
#     generateData.generateData(dimension[i], seed[i], option, minimum[i], maximum[i])
#     file = 'TSP_Data/random_instance_file.tsp'
#     instance = readData.ReadData(file)
#     size = instance.size
#     dis_mat = instance.GetDistanceMat()
#     # #gdybanie nad najlepszym wynikiem
#     bestpath = nearestNeigbor2.run(size, dis_mat)
#     bestpath = Opt2.Opt2(instance, bestpath)
#     bestdistance = calcTour.fc(dis_mat, bestpath)
#     # #koniec gdybania
#     list1 =[]
#     list2 =[]
#     list3 =[]
#
#     for k in range(1, 101):
#         time1 = time.time()
#         # print(dis_mat)
#         path = nearestNeigbor2.run(size, dis_mat, k)
#         print(k)
#         time2 = time.time()
#         timediff = time2 - time1
#         dystans = calcTour.fc(dis_mat, path)
#         if dystans<bestdistance:
#             bestdistance = dystans
#         list1.append(str(k) )
#         list2.append(dystans)
#         list3.append(str(timediff))
#
#     with open('Wyniki2/' + file.replace('TSP_Data/', "") + str(i) + 'wyniki.csv', 'w') as data:
#         for i in range(len(list1)):
#
#             prd = calcTour.PRD(list2[i], bestdistance)
#             data.write(list1[i] + '; '+ str(prd) +'; '+ list3[i] +' \n')