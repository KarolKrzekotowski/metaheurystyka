from random import randint,random
from Roulette import Roulette
import Paths
import krandom

from copy import copy, deepcopy
from Paths import fc

#klasa definiuje członka populacji
class Member():
    def __init__(self, permutation, pfc, death):
        self.perm = permutation
        self.fc = pfc
        self.death = death

    #wyświetl osobnika
    def print(self):
        print(f"{self.perm}: {self.fc}")
    #funkcja porównująca
    def __lt__(self, other):
        return self.fc < other.fc


class Island():
    def __init__(self, populationSize, instance,r_cross, lifeExpectancy,name="Unnamed"):
        #rozmiar populacji początkowej
        self.populationSize = populationSize
        #populacja
        self.population = []
        self.name = name
        self.generation = 0
        self.roulette = Roulette(self.populationSize)
        self.instance = instance
        self.lifeExpectancy = lifeExpectancy
        self.generateMembers(self.populationSize)
        self.r_cross = r_cross
        
        
    #wygenereuj populację o danym rozmiarze
    #(random? (na razie))
    def generateMembers(self, amount):
        for _ in range(amount):
            member,mfc = krandom.krandom(self.instance.size,self.instance.dis_mat,1)
            newMember = Member(member,mfc,self.generation + self.lifeExpectancy)
            self.population.append(newMember)
        self.population.sort()
        #print(f"Welcome {amount} new members to island {self.name}!")

    #funkcja wykonuje selekcję członków za pomocą ruletki
    def select(self, amount):
        selected = []
        for _ in range(amount):
            ix = self.roulette.getOne()
            selected.append(self.population[ix])

        return selected


    def create_child(self,p1, p2, point) -> "childer":
        c = p1.perm[0:point]

        for i in range(0,len(p1.perm)):
            if p2.perm[i] not in c:
                c.append(p2.perm[i])
        return c
    #krzyżowanie osobników
    def crossover(self,parents):
        children = []
        r_cross = self.r_cross
        #TODO
        #zwraca tablice members

        parents = deepcopy(parents)
        parents: [Member,Member] = [[parents[i],parents[i+1]]for i in range(0,len(parents), 2)]
        for p in parents:

            if random() < r_cross:
                # losowy punkt krzyżowania
                pt = randint(1,len(p[0].perm)-2)
                # dziecko 1
                c1 = self.create_child(p[0],p[1],pt)
                c1 = Member(c1, fc(self.instance.dis_mat,c1), self.generation + self.lifeExpectancy)
                children.append(c1)
                # dziecko 2
                c2 = self.create_child(p[1],p[0],pt)
                c2 = Member(c2, fc(self.instance.dis_mat,c2), self.generation + self.lifeExpectancy)
                children.append(c2)



            else:
                c1 = Member(p[0].perm,p[0].fc,self.generation + self.lifeExpectancy)
                children.append(c1)

                c2 = Member(p[1].perm, p[1].fc, self.generation + self.lifeExpectancy)
                children.append(c2)
        return children

    #"ukradnij" osobników do migracji (szansa ruletką)
    def stealMembers(self,amount):
        stolenIx = []
        stolen = []
        for _ in range(amount):
            ix = self.roulette.getOne()
            stolen.append(self.population[ix])
            stolenIx.append(ix)

        stolenIx.sort(reverse=True)
        

        for s in stolenIx:
            print(stolenIx)
            self.population.pop(s)

        return stolen

    #funkcja wstawia osobnika do posortowanej listy w czasie O(log(n))
    def putInOrder(self, newMember):
        ixs = 0
        ixe = len(self.population)-1
        while True:
            
            if ixe-ixs <= 1: break
            mid = int((ixs+ixe)/2)
            if self.population[mid].fc < newMember.fc:
                ixs = mid
            elif self.population[mid].fc > newMember.fc:
                ixe = mid
            else:
                break
        sfc = self.population[ixs].fc
        efc = self.population[ixe].fc

        if sfc > newMember.fc:
            self.population.insert(ixs,newMember)
        elif efc < newMember.fc:
            self.population.insert(ixe+1,newMember)
        else:
            self.population.insert(ixe,newMember)

    #mutacja (każdy osobnik rozpatrzany osobno)
    # chance = szansa mutacji
    def mutate(self, chance:float):
        for i in range(self.populationSize):
            if random() < chance:
                #print(f"Mutation of member {i}!")

                #wyizoluj osobnika
                mb = self.population[i]
                self.population.pop(i)
                
                #mutacja
                r1 = randint(0,self.instance.size-1)
                r2 = randint(0,self.instance.size-1)
                if r1>r2: (r1,r2) = (r2,r1)
                newpath = Paths.swap(mb.perm,r1,r2)
                mb.perm = newpath

                #wstaw ponownie
                mb.fc = Paths.fc(self.instance.dis_mat,mb.perm)
                self.putInOrder(mb)
        pass
    
    #zdarzenie wymierania najsłabszych osobników na wyspie
    # chance - szansa na eksterminację
    def nukeWorst(self,chance:float):
        #ilość wymarłych osobników
        nukedNb = int(self.populationSize * chance)
        for _ in range(nukedNb):
            self.population.pop(-1)
        self.generateMembers(nukedNb)
    
    #zdarzenie wymierania losowych osobników na wyspie
    # chance - szansa na eksterminację
    def nukeRandom(self,chance:float):
        #ilość wymarłych osobników
        nukedNb = int(self.populationSize * chance)
        for i in range(nukedNb):
            r = randint(0,self.populationSize-i-1)
            self.population.pop(r)
        self.generateMembers(nukedNb)
    
    #oblicz "wartość" wyspy (sumę funkcji celu populacji)
    def islandValue(self):
        s=0
        for p in self.population:
            s+=p.fc
        return s
