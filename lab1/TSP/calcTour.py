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
