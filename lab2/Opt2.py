import Paths
import copy
#funkcja tworzy permutację ścieżki z inwersją od punktu a do b
def invert(path,a,b):
    newpath = path.copy()

    while a<b:
        newpath[a] = path[b]
        newpath[b] = path[a]
        a+=1
        b-=1
    
    return newpath

def Opt2(instance, path):
    #pobierz informacje
    size = instance.size
    mat = copy.deepcopy(instance.dis_mat)

    #koszt optymalnej drogi dla wszystkich instancji
    bestfc = Paths.fc(mat,path)

    while True:
        #zmienne przechowują najlepszy wynik instancji
        insfc = bestfc
        inspath = path

        #przejdź wszystkie permutacje (inwersje)
        for i in range(0,size):
            for j in range(i+1,size):
                p = invert(path,i,j)
                t = Paths.fc(mat,p)
                #najlepsza ścieżka instancji
                if t<insfc:
                    insfc = t
                    inspath = p
        #exit loop
        if insfc==bestfc: break

        #kontynuuj pętle jeśli da się poprawić
        path = inspath
        bestfc = insfc

    return path
