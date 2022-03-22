import matplotlib.pyplot as plt

#kolor punktów na grafie
PTScolor = "gold"
#kolor linii na grafie
LINEcolor = "dimgrey"

#wyświetl macierz w podany sposób
def matPrint(mat):
    for i in range(0,len(mat)):
        print(f"[{i}]", end="\t")
        print(*mat[i], sep="\t")

#funkcja zwraca ścieżkę z podanego pliku .opt.tour
def loadPath(filedir):
    try:
        path = list()
        with open(f'{filedir}') as data:
            splitData = data.read().split()

            #przejdź plik aż do początku ścieżki
            for i,elem in enumerate(splitData):
                if elem == "TOUR_SECTION":
                    iv = i+1
                    break

            #ścieżka kończy się liczbą -1, czasami też EOF
            while splitData[iv] != "-1":
                path.append(int(splitData[iv]))
                iv+=1
        #dokończ cykl
        path.append(path[0])
        return path
    except:
        print("Error when loading file:",filedir)

#wyświetl ścieżkę dla podanej instancji na konsoli
def printPath(mat,path):
    l = len(path)
    for i in range(0,l-1):
        print(path[i],"\t--[",mat[path[i]-1][path[i+1]-1],"]->\t",path[i+1])
    print(path[l-1],"\t--[",mat[path[l-1]-1][path[0]-1],"]->\t",path[0])


#funkcja tworzy graf dla podanej instancji i ścieżki (instancja musi być typu EUC_2D)
def EUCgraph(instance,path):

    if instance.EdgeWeightType != "EUC_2D":
        print("Wrong graph type! (Not EUC_2D)")
        return

    #dane punktów
    points = instance.read_Data()
    xpts = list()
    ypts = list()

    for i,x,y in points:
        xpts.append(x)
        ypts.append(y)
    
    l = len(path)
    #rysuj ścieżki
    for i in range(0,l-1):
        xc = [xpts[path[i]-1],xpts[path[i+1]-1]]
        yc = [ypts[path[i]-1],ypts[path[i+1]-1]]
        plt.plot(xc,yc,color=LINEcolor)
    xc = [xpts[path[l-1]-1],xpts[path[0]-1]]
    yc = [ypts[path[l-1]-1],ypts[path[0]-1]]
    plt.plot(xc,yc,color=LINEcolor)

    plt.scatter(xpts,ypts, color=PTScolor)

    for i,x,y in points:
        plt.annotate(i,(x,y))

    plt.show()