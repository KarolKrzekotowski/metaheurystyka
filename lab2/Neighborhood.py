import Paths
import random

class Neighborhood:
    def __init__(self,pathSize):
        self.pathSize = pathSize
        #do dostrojenia
        self.hoodSize = 420
        self.stallLimit = 5

    def get(self):
        #słownik sprawdza czy nie wykonaliśmy już danego inverta 
        dict = {}
        arr = []
        stall = 0
        for i in range(0,self.hoodSize):
            r1 = random.randint(0,self.pathSize-1)
            while(True):
                r2 = random.randint(0,self.pathSize-1)
                if r1 != r2: break
            if r1>r2:
                (r1,r2)=(r2,r1)
            #klucz unikalny dla każdej pary
            key = r1 + r2*self.pathSize
            
            if key in dict:
                #potwórz krok
                i=i-1
                stall=stall+1
                #wyjdź z utknięcia - przerwij pętlę
                if (stall >= self.stallLimit):
                    break
                continue

            stall = 0
            dict[key]=True
            arr.append([r1,r2])

        return arr
