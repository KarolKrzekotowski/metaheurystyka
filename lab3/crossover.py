import random
import sys


def OX(p1, p2, r1, r2) -> []:
    # lista wypełniona -100
    c1 = [-100] * len(p1)
    # środek rodzica 2
    c2_inside = p2[r1:r2 + 1]
    # prawa ręka rodzica 2
    c2_right = p2[r2 + 1:]
    # lewa ręka rodzica 2
    c2_left = p2[0:r1]
    # right -> left -> inside
    merged_c1 = c2_right + c2_left + c2_inside

    # wpisanie wycięcie korpusu rodzica 1
    for e in range(r1, r2 + 1):
        c1[e] = p1[e]
    # lista niepowtarzających się elementów
    d1 = []
    for i in merged_c1:
        if i not in c1:
            d1.append(i)
    # wszycie prawej ręki do ciała dziecka

    for i in range(r2 + 1, len(c1)):
        c1[i] = d1[0]
        d1.pop(0)
    # wszycie lewej ręki do ciała dziecka

    for i in range(r1):
        c1[i] = d1[0]
        d1.pop(0)

    return c1
import numpy as np
def PMX(parent1,parent2,firstCrossPoint,secondCrossPoint):
    parent1MiddleCross = parent1[firstCrossPoint:secondCrossPoint]
    parent2MiddleCross = parent2[firstCrossPoint:secondCrossPoint]

    print(parent1)
    print(parent2)
    print(firstCrossPoint)
    print(secondCrossPoint)
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(1000000)
    temp_child1 = parent1[:firstCrossPoint] + parent2MiddleCross + parent1[secondCrossPoint:]
    temp_child2 = parent2[:firstCrossPoint] + parent1MiddleCross + parent2[secondCrossPoint:]
    relations = []
    for i in range(len(parent1MiddleCross)):
        relations.append([parent2MiddleCross[i], parent1MiddleCross[i]])
    print('hej1')
    c1 = recursion1(temp_child1,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross,relations,parent1,parent2)
    print('hej2')
    for i in relations:
        i = i.reverse()
    c2 = recursion1(temp_child2,firstCrossPoint,secondCrossPoint,parent2MiddleCross,parent1MiddleCross,relations,parent2,parent1)
    print('hej3')
    return c1,c2


def recursion1 (temp_child , firstCrossPoint , secondCrossPoint , parent1MiddleCross , parent2MiddleCross,relations,parent1,parent2) :
    child = np.array([0 for i in range(len(parent1))])
    for i,j in enumerate(temp_child[:firstCrossPoint]):
        c=0
        for x in relations:
            if j == x[0]:
                child[i]=x[1]
                c=1
                break
        if c==0:
            child[i]=j
    j=0
    for i in range(firstCrossPoint,secondCrossPoint):
        child[i]=parent2MiddleCross[j]
        j+=1

    for i,j in enumerate(temp_child[secondCrossPoint:]):
        c=0
        for x in relations:
            if j == x[0]:
                child[i+secondCrossPoint]=x[1]
                c=1
                break
        if c==0:
            child[i+secondCrossPoint]=j
    child_unique=np.unique(child)
    if len(child)>len(child_unique):
        child=recursion1(temp_child , firstCrossPoint , secondCrossPoint , parent1MiddleCross , parent2MiddleCross,relations,parent1,parent2)
    return(child)
#single point
def SPX(p1,p2,point):
    c = p1[0:point]

    for i in range(0, len(p1)):
        if p2[i] not in c:
            c.append(p2[i])
    return c

# cycle crossover 2(CX2)
def indexOf(arr,x):
    for a in range(0,arr.__len__()):
        if arr[a] == x:
            return a
    return -1

def findUnusedIndexValues(parent,offspring):
    res = list()
    for a in parent:
        if indexOf(offspring,a) == -1:
            res.append(a)
    return res

def CX( parent1, parent2 ):
    cycles = [-1] * len(parent1)
    cycle_no = 1
    cyclestart = (i for i, v in enumerate(cycles) if v < 0)
    for pos in cyclestart:
        while cycles[pos] < 0:
            cycles[pos] = cycle_no
            pos = parent1.index(parent2[pos])
        cycle_no += 1
    child1 = [parent1[i] if n % 2 else parent2[i] for i, n in enumerate(cycles)]
    child2 = [parent2[i] if n % 2 else parent1[i] for i, n in enumerate(cycles)]
    return child1,child2

if __name__ == 'main':

    a = [1,2,3,4,5,6,7,8,9,10]
    b = [4,3,1,2,8,7,10,5,6,9]
    p = 3
    q = 6
    x ,y = PMX(a,b,p,q)
    print(x)
    print(y)
