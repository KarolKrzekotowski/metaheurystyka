import random
from xmlrpc.client import MAXINT
import calcTour

def krandom(size,mat,k=10):


    min = MAXINT
    minlist = list()

    for i in range(0,k):
        path = list(range(1,size+1))
        for j in range(0,size):
            a = random.randint(0,size-1)
            b = random.randint(0,size-1)
            if a!=b:
                path[a],path[b] = path[b],path[a]
            t = calcTour.fc(mat,path)
        if t < min:
            min = t
            minlist = path
    return minlist

#krandom(None,10)

