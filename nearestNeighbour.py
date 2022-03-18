import time
import copy
import numpy as np
import random
import readData
start_time = time.time()

def run(size,dis_mat,start_point):

    path_index = [start_point]
    changed_path = copy.copy(dis_mat)
    for i in range(size):
        changed_path[i][i] = 999999999
    path_index.append( np.argmin(changed_path[start_point]))
    for i in range(size):
        changed_path[i][start_point] = 999999999
    distance = dis_mat[start_point][path_index[1]]
    i = 2
    while i != size:
        last_element = path_index[-1]
        # zmiana ostatnio użytego elementu na maksymalny, żeby nie został użyty
        for j in changed_path:
            j[last_element] = 999999999
        path_index.append( np.argmin(changed_path[last_element]))
        distance += dis_mat[last_element][path_index[-1]]
        i += 1
    distance += dis_mat[path_index[0]][path_index[-1]]
    path_index = [1 + x for x in path_index]
    return path_index, distance



