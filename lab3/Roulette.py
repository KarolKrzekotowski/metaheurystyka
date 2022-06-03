import math
from random import randint

#rozkład przedziałów ruletki (musi sumować się do 100)
rouletteInterval = [10,20,50,20]
#stotunek wybrania dla danych przedziałów
rouletteChance = [4,2,1,1]

class Roulette():
    def __init__(self, size):
        if len(rouletteInterval) != len(rouletteChance):
            print("BŁĄD: długości tabel ruletki nie zgadzają się!")
            exit(-1)
        if sum(rouletteInterval) != 100:
            print("BŁĄD: przedziały ruletki nie sumują się do 100!")
            exit(-1)
        #rozmiar populacji
        self.size = size
        #zasięg przedziałów
        self.ivlRngs = []
        #suma wartości przedziałów
        self.sum = 0
        #ilość przedziałów
        self.ivlNb = len(rouletteInterval)
        #ilość członków każdego przedziału
        self.ivlMbs = []

        #wygeneruj przedziały
        tsum = 0
        for i in range(len(rouletteInterval)-1):
            members = round(size*rouletteInterval[i]/100.0)
            s = members*rouletteChance[i]
            self.sum += s
            self.ivlRngs.append(s)
            self.ivlMbs.append(members)
            tsum += members
        #ostatni przedział
        remaining = size - tsum
        s = remaining*rouletteChance[-1]
        self.sum += s
        self.ivlRngs.append(s)
        self.ivlMbs.append(remaining)
        print(self.ivlRngs)
        print(self.ivlMbs)
    
    #pobierz jeden element z ruletki
    def getOne(self):
        r = randint(0,self.sum-1)

        i=0
        isum = 0
        mbs = 0
        while True:
            isum += self.ivlRngs[i]
            mbs += self.ivlMbs[i]
            if r < isum:
                break
            i+=1
            
        diff = isum - r
        dn = math.ceil(diff/rouletteChance[i])
        return mbs-dn 

    #pobierz wiele elementów (możliwe powtórzenia)
    def getMany(self,amount):
        list = []
        for _ in range(amount):
            e = self.getOne()
            list.append(e)
        return list
