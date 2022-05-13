from tabu2 import TabuSearch
import normalTabu
from Paths import swap, invert, fc
from readData import ReadData
import random
import nearestNeighbour
import nearestNeigbor2
import Opt2
import sys
import contextlib

tsp_files = ['berlin52.tsp', 'ch150.tsp', 'gr48.tsp', 'pr107.tsp']
atsp_files = ['ftv70.atsp', 'br17.atsp', 'ft53.atsp', 'ftv170.atsp']

tabu_size = 100
max_iterations = 1500
methods = {
    'swap': swap,
    'invert': invert
}

# for i in tsp_files:
#     instance = ReadData('TSP_Data/' + i)
#     size = instance.size
#     dis_mat = instance.GetDistanceMat()
#     start = random.randint(0, size - 1)
#     path, _ = nearestNeighbour.run(size, dis_mat, start)
#     distance = fc(dis_mat, path)
#     halo = TabuSearch(distance, path, dis_mat)
#
#     for j in range(5,16,2):
#         with open('Wynik4/'+ i + "invert" + 'NNrozmiarLongMemory'+ str(j) , 'w') as o:
#             with contextlib.redirect_stdout(o):
#                 o.write("iteracja; zmiana najlepszego \n ")
#                 halo = TabuSearch(distance, path, dis_mat)
#                 halo.run(max_iterations,tabu_size,j,invert)

# for i in atsp_files:
#     instance = ReadData('TSP_Data/' + i, True)
#     size = instance.size
#     dis_mat = instance.dis_mat
#     start = random.randint(0, size - 1)
#     path, _ = nearestNeighbour.run(size, dis_mat, start)
#     distance = fc(dis_mat, path)
#     halo = TabuSearch(distance, path, dis_mat)
#
#     for j in range(5,16,2):
#         with open('Wynik4/' + i + "invert" + 'NNtrozmiarLongMemory' + str(j), 'w') as o:
#             with contextlib.redirect_stdout(o):
#                 o.write("iteracja; zmiana najlepszego \n")
#                 halo = TabuSearch(distance, path, dis_mat)
#                 halo.run(max_iterations, tabu_size,j, invert)



# for i in tsp_files:
#     instance = ReadData('TSP_Data/' + i)
#     size = instance.size
#     dis_mat = instance.GetDistanceMat()
#     start = random.randint(0, size - 1)
#     path, _ = nearestNeighbour.run(size, dis_mat, start)
#     distance = fc(dis_mat, path)
#     halo = normalTabu.TabuSearch(distance, path, dis_mat)
#
#     for j in range(0,10):
#         with open('Wynik6/'+ i + "invert" + 'NNnormalnaInvert'+ str(j) , 'w') as o:
#             with contextlib.redirect_stdout(o):
#                 o.write("iteracja; zmiana najlepszego \n ")
#                 halo = normalTabu.TabuSearch(distance, path, dis_mat)
#                 halo.run(max_iterations,tabu_size)



# for i in atsp_files:
#     instance = ReadData('TSP_Data/' + i, True)
#     size = instance.size
#     dis_mat = instance.dis_mat
#     start = random.randint(0, size - 1)
#     path, _ = nearestNeighbour.run(size, dis_mat, start)
#     distance = fc(dis_mat, path)
#     halo = normalTabu.TabuSearch(distance, path, dis_mat)
#
#     for j in range(0, 10):
#         with open('Wynik6/' + i + "invert" + 'NNnormalnaInvert' + str(j), 'w') as o:
#             with contextlib.redirect_stdout(o):
#                 o.write("iteracja; zmiana najlepszego \n")
#                 halo = normalTabu.TabuSearch(distance, path, dis_mat)
#                 halo.run(max_iterations, tabu_size)


# for i in tsp_files:
#     instance = ReadData('TSP_Data/' + i)
#     size = instance.size
#     dis_mat = instance.GetDistanceMat()
#     start = random.randint(0, size - 1)
#     path, _ = nearestNeighbour.run(size, dis_mat, start)
#     distance = fc(dis_mat, path)
#     halo = TabuSearch(distance, path, dis_mat)
#
#     for j in range(10,310,10):
#         with open('Wynik2/'+ i + "invert" + 'NNtaburozmiar'+ str(j) , 'w') as o:
#             with contextlib.redirect_stdout(o):
#                 o.write("iteracja; zmiana najlepszego \n ")
#                 halo = TabuSearch(distance, path, dis_mat)
#                 halo.run(max_iterations,j,invert)



# for i in atsp_files:
#     instance = ReadData('TSP_Data/' + i, True)
#     size = instance.size
#     dis_mat = instance.dis_mat
#     start = random.randint(0, size - 1)
#     path, _ = nearestNeighbour.run(size, dis_mat, start)
#     distance = fc(dis_mat, path)
#     halo = TabuSearch(distance, path, dis_mat)
#
#     for j in range( 10, 310,10):
#         with open('Wynik2/' + i + "swap" + 'NNtaburozmiar' + str(j), 'w') as o:
#             with contextlib.redirect_stdout(o):
#                 o.write("iteracja; zmiana najlepszego \n")
#                 halo = TabuSearch(distance, path, dis_mat)
#                 halo.run(max_iterations, tabu_size, swap)

# for i in atsp_files:
#     instance = ReadData('TSP_Data/' + i, True)
#     size = instance.size
#     dis_mat = instance.dis_mat
#     start = random.randint(0, size - 1)
#     path, _ = nearestNeighbour.run(size, dis_mat, start)
#     distance = fc(dis_mat, path)
#     halo = TabuSearch(distance, path, dis_mat)
#
#     for j in range(0, 10):
#         with open('Wynik1/' + i + "invert" + 'NN' + str(j), 'w') as o:
#             with contextlib.redirect_stdout(o):
#                 o.write("iteracja; zmiana najlepszego \n")
#                 halo = TabuSearch(distance, path, dis_mat)
#                 halo.run(max_iterations, tabu_size, invert)
#     for j in range(10, 20):
#         with open('Wynik1/' + i + "swap" + 'NN' + str(j), 'w') as o:
#             with contextlib.redirect_stdout(o):
#                 o.write("iteracja; zmiana najlepszego\n ")
#                 halo = TabuSearch(distance, path, dis_mat)
#                 halo.run(max_iterations, tabu_size, swap)
#
#     path = nearestNeigbor2.run(size, dis_mat, 0)
#     path = Opt2.Opt2(instance, path, True)
#
#     for j in range(0, 10):
#         with open('Wynik1/' + i + "invert" + 'OPT2' + str(j), 'w') as o:
#             with contextlib.redirect_stdout(o):
#                 o.write("iteracja; zmiana najlepszego \n ")
#                 halo = TabuSearch(distance, path, dis_mat)
#                 halo.run(max_iterations, tabu_size, invert)
#     for j in range(10, 20):
#         with open('Wynik1/' + i + "swap" + 'OPT2' + str(j), 'w') as o:
#             with contextlib.redirect_stdout(o):
#                 o.write("iteracja; zmiana najlepszego \n")
#                 halo = TabuSearch(distance, path, dis_mat)
#                 halo.run(max_iterations, tabu_size, swap)



# for i in tsp_files:
#     instance = ReadData('TSP_Data/' + i)
#     size = instance.size
#     dis_mat = instance.GetDistanceMat()
#     start = random.randint(0, size - 1)
#     path, _ = nearestNeighbour.run(size, dis_mat, start)
#     distance = fc(dis_mat, path)
#     halo = TabuSearch(distance, path, dis_mat)
#
#     for j in range(0,10):
#         with open('Wynik1/'+ i + "invert" + 'NN'+ str(j) , 'w') as o:
#             with contextlib.redirect_stdout(o):
#                 o.write("iteracja; zmiana najlepszego \n ")
#                 halo = TabuSearch(distance, path, dis_mat)
#                 halo.run(max_iterations,tabu_size,invert)
#     for j in range(10,20):
#         with open('Wynik1/' + i + "swap" + 'NN' + str(j), 'w') as o:
#             with contextlib.redirect_stdout(o):
#                 o.write("iteracja; zmiana najlepszego \n ")
#                 halo = TabuSearch(distance, path, dis_mat)
#                 halo.run(max_iterations, tabu_size, swap)
#
#     path = nearestNeigbor2.run(size, dis_mat, 0)
#     path = Opt2.Opt2(instance, path, True)
#
#     for j in range(0, 10):
#         with open('Wynik1/' + i + "invert" + 'OPT2' + str(j), 'w') as o:
#             with contextlib.redirect_stdout(o):
#                 o.write("iteracja; zmiana najlepszego  \n")
#                 halo = TabuSearch(distance, path, dis_mat)
#                 halo.run(max_iterations, tabu_size, invert)
#     for j in range(10, 20):
#         with open('Wynik1/' + i + "swap" + 'OPT2' + str(j), 'w') as o:
#             with contextlib.redirect_stdout(o):
#                 o.write("iteracja; zmiana najlepszego \n")
#                 halo = TabuSearch(distance, path, dis_mat)
#                 halo.run(max_iterations, tabu_size, swap)
