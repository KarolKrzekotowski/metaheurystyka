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


    sys.setrecursionlimit(1000000)
    temp_child1 = parent1[:firstCrossPoint] + parent2MiddleCross + parent1[secondCrossPoint:]
    temp_child2 = parent2[:firstCrossPoint] + parent1MiddleCross + parent2[secondCrossPoint:]
    relations = []
    for i in range(len(parent1MiddleCross)):
        relations.append([parent2MiddleCross[i], parent1MiddleCross[i]])

    c1 = recursion1(temp_child1,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross,relations,parent1,parent2)

    for i in relations:
        i = i.reverse()
    c2 = recursion1(temp_child2,firstCrossPoint,secondCrossPoint,parent2MiddleCross,parent1MiddleCross,relations,parent2,parent1)

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

# cycle crossover(CX)



def indexOf(arr,x):
    for a in range(0,arr.__len__()):
        if arr[a] == x:
            return a
    return -1

def fillNoneWithSwappedValue(arr1 ,arr2 ,final1 ,final2 ):
    for a in range(0,arr1.__len__()):
        if final1[a] == None:
            final1[a] = arr2[a]
        if final2[a] == None:
            final2[a] = arr1[a]
    return final1,final2
def crossoverOperator( parent1, parent2 ):
    offspring1 = [None] * parent1.__len__()
    offspring2 = [None] * parent2.__len__()
    size1 = 1
    size2 = 1

    initalSelected = parent1[0]
    offspring1[0] = parent1[0]
    latestUpdated2 = parent2[0]
    check = 1

    while size1 < parent1.__len__() or size2 < parent2.__len__():
        # jeśli ostatnio zmieniony  to wartość inicjująca - koniec działania, cykl ma pętle
        if latestUpdated2 == initalSelected:
            # index rodzica2 gdzie wystepuje lastupdated2
            index2 = indexOf(parent2,latestUpdated2)
            # dziecko2 od index2 przyjmuje wartość rddzica2  w tym miejscu
            offspring2[index2] = parent2[index2]
            #wypełniamy nieodwiedzone miejsca liczbami z rodziców
            ans1,ans2 = fillNoneWithSwappedValue(parent1, parent2, offspring1, offspring2)
            offspring1 = ans1
            offspring2 = ans2
            size1 = parent1.__len__()
            size2 = parent2.__len__()
            check = 0
        else:
            # index rodzica2, gdzie występuje wartość lastupdated2
            index2 = indexOf(parent2,latestUpdated2)
            #dziecko2 od indeksu2 przyjmuje wartość rodzica w tym indexie, zwiększamy rozmiar liczb w dziecku2
            offspring2[index2] = parent2[index2]
            size2 += 1
            #index1 to indeks gdzie w rodzicu1 znajduje się wartość dodana do listy dziecko2
            index1 = indexOf(parent1,parent2[index2])
            # zapisujemy tę wartość do dziecko1 w tym indexie, zwiększamy rozmiar liczb w dziecku1
            offspring1[index1] = parent1[index1]
            size1 += 1
            # lastUpdated2 przyjmuje wartość rodzica2  w indeks1
            latestUpdated2 = parent2[index1]
    if check:
        index2 = indexOf(parent2, latestUpdated2)
        offspring2[index2] = parent2[index2]

    return offspring1,offspring2


if __name__ == '__main__':

    a = [1,2,3,4,5,6,7,8]
    b = [8, 5, 2, 1, 3, 6, 4, 7]
    ans,ans2 = crossoverOperator(a,b )




