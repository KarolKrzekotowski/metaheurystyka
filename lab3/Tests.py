import Island

#znajdź najlepszą wartość dla danej generacji
def getValueAt(gen,Improvements):
    ix = -1
    while ix+1 < len(Improvements):
        mb = Improvements[ix+1]
        if mb[0]>gen:
            break
        ix += 1
        
    return Improvements[ix][1]

def getFinal(Improvements):
    return Improvements[-1][1]
