#Klasa GeneticAlgorithm odpowiada za zarządzanie wyspami podczas symulacji

import sys
from xmlrpc.client import boolean
import readData
import random
from Paths import PRD
import Island

#rozmiar populacji na wyspach
POPULATION_SIZE = 20
#szansa wydarzenia wymierania
NUKE_CHANCE = 0.001
#ilość populacji usuniętej podczas wymierania
NUKE_AMOUNT = 0.75
#szansa na migrację
MIGRATION_CHANCE = 0.02
#ilość migrujących osobników
MIGRATING_MEMBERS = int(POPULATION_SIZE/10)
#ilość rodziców
PARENTS_SIZE = int(POPULATION_SIZE/2)
#ilość członków "elitarnych"
ELITES = 3
#gromadzenie najlepszych wyników
gen_best = []


class GeneticAlgorithm():
    '''   
    Klasa przyjmuje następujące parametry:
        generations - liczba generacji
        islandNb - liczba wysp
        instance - odniesienie do instancji grafu i macierzy
        r_cross - szansa krzyżowania rodziców
        xmode - tryb krzyżowania
        useInvert - określenie czy mamy używać invert czy swap jako metodę mutacji
        MUTATION_CHANCE - szansa mutacji każdego osobnika
        ratio - stosunek początkowej populacji NN a KRandom (1 to w pełni KRandom)
        LIFE_EXPECTANCY - maksymalna długość życia osobnika
    '''
    def __init__(self, generations, islandNb, instance,r_cross,xmode,useInvert,MUTATION_CHANCE=0.06,ratio=0.2,LIFE_EXPECTANCY=50):
        self.generationNb = generations
        self.islandNb = islandNb
        self.instance = instance
        self.useInvert = useInvert
        self.xmode = xmode
        self.MUTATION_CHANCE = MUTATION_CHANCE
        self.LIFE_EXPECTANCY = LIFE_EXPECTANCY

        #aktualna generacja
        self.generation = 0
        #zbiór wysp
        self.ISLANDS = []
        #najlepsza globalnie permutacja
        self.bestPerm = []
        self.bestFC = sys.float_info.max
    
        #przechowywane poprawy
        self.Improvements = []
        
        #inicjuj wyspy
        for i in range(islandNb):
            self.ISLANDS.append(Island.Island(POPULATION_SIZE,self.instance, r_cross,self.LIFE_EXPECTANCY, "Wyspa "+str(i),ratio=ratio))

    # utwórz nieposortowaną populację
    def createPopulation(self, population, parents, children):
        #bierzemy podział elity + 1:2:2
        newPopulation = []
        
        #elity
        for i in range(0,ELITES):
            if population[i].death > self.generation:
                newPopulation.append(population[i])

        remaining = POPULATION_SIZE-len(newPopulation)
        pcNb = int(remaining*2/5)

        #rodzice
        pcLen = len(parents)
        for i in range(pcNb):
            r = random.randint(0,pcLen-1)
            if parents[r].death > self.generation:
                newPopulation.append(parents[r])

        #dzieci
        pcLen = len(children)
        for i in range(pcNb):

            r = random.randint(0,pcLen-1)
            newPopulation.append(children[r])

        #reszta
        remaining = POPULATION_SIZE - len(newPopulation)
        while remaining > 0:
            r = random.randint(0,POPULATION_SIZE-1)
            if population[r].death > self.generation:
                newPopulation.append(population[r])
                remaining-=1

        return newPopulation

    #symuluj wszystkie wyspy przez podaną w konstruktorze ilość generacji
    def simulate(self,bestSolution=0,debug:boolean=False):
        for i in range(self.generationNb):
            #print(f"Gen {i}")
            self.simulateGeneration(bestSolution,debug)
        if debug:
            print(self.bestPerm)
        return self.Improvements

    #wypisz najlepszy wynik
    def printBest(self):
        print(f"[{self.bestFC}] {self.bestPerm}")

    #pobierz najlepszy wynik
    def GetGenBest(self):
        return gen_best

    '''
        Przeprowadź symulację generacji w następującym cyklu:
            1. Zdarzenia losowe (migracja, wymieranie)
            2. Wybór rodziców
            3. Krzyżowanie
            4. Nowa populacjia
            5. Mutacja
            6. Sortuj
    '''
    def simulateGeneration(self,bestSolution=0,debug:boolean=False):
        #nowa generacja
        self.generation += 1
        for ISLAND in self.ISLANDS:
            ISLAND.generation = self.generation

        #wymieranie najgorszej wyspy
        if random.random() < NUKE_CHANCE:
            highest = 0
            hix = -1
            for i in range(len(self.ISLANDS)):
                ifc = self.ISLANDS[i].islandValue()
                if ifc > highest:
                    highest = ifc
                    hix = i
            #print(f"Wymieranie na wyspie: {self.ISLANDS[hix].name}")
            self.ISLANDS[hix].nukeRandom(0.8)

        #migracja pomiędzy dwoma wyspami
        x = random.random()
        if x < MIGRATION_CHANCE:
            r1 = random.randint(0,self.islandNb-1)
            r2 = random.randint(0,self.islandNb-1)

            if r1 != r2:
                #print(f"Migracja pomiędzy {self.ISLANDS[r1].name} a {self.ISLANDS[r2].name}")
                migrantsA = self.ISLANDS[r1].stealMembers(MIGRATING_MEMBERS)
                migrantsB = self.ISLANDS[r2].stealMembers(MIGRATING_MEMBERS)
                for m in migrantsB:
                    self.ISLANDS[r1].population.append(m)
                self.ISLANDS[r1].population.sort()
                for m in migrantsA:
                    self.ISLANDS[r2].population.append(m)
                self.ISLANDS[r2].population.sort()

        #głowny przebieg wyspy
        for ISLAND in self.ISLANDS:
            #wybór rodziców (ruletka)
            parents = ISLAND.select(PARENTS_SIZE)
            #krzyżowanie (OX,PMX,SPX)
            children = ISLAND.crossover(parents,self.xmode)
            
            #utworzenie nowej populacji (nieposortowana)
            new_population = self.createPopulation(ISLAND.population,parents,children)
            ISLAND.population = new_population
            #mutowanie nowej populacji (nieposortowana)
            ISLAND.mutate(self.MUTATION_CHANCE, self.useInvert)

            #sortowanie populacji
            ISLAND.population.sort()
            

            #print("best",ISLAND.name,"=",ISLAND.population[0].fc)
            if ISLAND.population[0].fc < self.bestFC:
                self.bestFC = ISLAND.population[0].fc
                self.bestPerm = ISLAND.population[0].perm
                self.Improvements.append([self.generation,self.bestFC])
                #do prezentacji
                if debug:
                    prd = PRD(self.bestFC,bestSolution)
                    print(f"{self.generation}\t{self.bestFC}\t{prd:.2f}%")

        if self.generation % 250 == 0 and self.generation > 1:

            gen_best.append(self.bestFC)




def test():
    file = sys.argv[1]
    if file[-4] == 'a':
        instance = readData.ReadData(file, True)
    else:
        instance = readData.ReadData(file)
    ox = 1
    pmx = 2
    spx = 3
    cx = 4

    GA = GeneticAlgorithm(10000,1,instance,0.5,cx,True,ratio=0.25)

    imp = GA.simulate(7542,True)
    # GA.printBest()
    # print(imp)
    print(imp[-1][1])
if __name__ == '__main__':
    test()
