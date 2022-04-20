#funkcja tworzy permutację ścieżki z inwersją od punktu a do b
def invert(path,a,b):
    newpath = path.copy()
    while a<b:
        newpath[a] = path[b]
        newpath[b] = path[a]
        a+=1
        b-=1
    return newpath

#funkcja tworzy permutację ścieżki z inwersją od punktu a do b
def swap(path,a,b):
    newpath = path.copy()
    temp = path[a]
    newpath[a] = newpath[b]
    newpath[b] = temp
    return newpath

'''
funkcja oblicza funkcję celu w zależności od stanu przed
(działa O(1) a nie O(n) w zależności od długości ścieżki)
    fc - wartość funkcji celu przed swapem
    mat - macierz z wartościami krawędzi
    path - ścieżka przed swapem
    a,b - zamieniane indeksy
    size - rozmiar ścieżki
'''
#może zostać użyta dla symetrycznego TSP invert
def fcSwap(fc,mat,path,a,b,size):
    newfc = fc
    i1 = (path[a-1]-1)%size
    i2 = (path[a+1]-1)%size
    #odepnij A
    newfc -= mat[i1][path[a]-1]
    newfc -= mat[path[a]-1][i2]
    #wstaw B w miejsce A
    newfc += mat[i1][path[b]-1]
    newfc += mat[path[b]-1][i2]
    i1 = (path[b-1]-1)%size
    i2 = (path[b+1]-1)%size
    #odepnij B
    newfc -= mat[i1][path[b]-1]
    newfc -= mat[path[b]-1][i2]
    #wstaw A w miejsce B
    newfc += mat[i1][path[a]-1]
    newfc += mat[path[a]-1][i2]

    return newfc

#funkcja liczy długość cyklu (wartość funkcji celu)
def fc(mat,path):
    l = len(path)
    fc = 0

    for i in range(0,l-1):
        p1 = path[i]
        p2 = path[i+1]
        w = mat[p1-1][p2-1]
        fc += w
    
    #dokończenie cyklu
    p1 = path[l-1]
    p2 = path[0]
    fc += mat[p1-1][p2-1]

    return fc

#wartość PRD
def PRD(fx,fref):
    return (fx-fref)/fref