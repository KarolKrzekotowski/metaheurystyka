from pickle import POP
import sys
import readData
import random
import Island

#rozmiar populacji na wyspach
POPULATION_SIZE = 100
#szansa wydarzenia wymierania
NUKE_CHANCE = 0.001
#ilość populacji usuniętej podczas wymierania
NUKE_AMOUNT = 0.8
#szansa na migrację
MIGRATION_CHANCE = 0.00
#ilość migrujących osobników
MIGRATING_MEMBERS = int(POPULATION_SIZE/10)
#ilość rodziców
PARENTS_SIZE = int(POPULATION_SIZE/2)
#ilość członków "elitarnych"
ELITES = 3
#szansa mutacji każdego osobnika
MUTATION_CHANCE = 1.0
#maksymalna ilość generacji danego osobnika
LIFE_EXPECTANCY = 10

class GeneticAlgorithm():
    def __init__(self, generations, islandNb, instance,r_cross):
        self.generation = 0
        self.generationNb = generations
        self.islandNb = islandNb
        self.ISLANDS = []
        self.instance = instance


        for i in range(islandNb):
            self.ISLANDS.append(Island.Island(POPULATION_SIZE,self.instance, r_cross,LIFE_EXPECTANCY, "Wyspa "+str(i)))

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

        newPopulation.sort()
        return newPopulation

    def simulate(self):
        for i in range(self.generationNb):
            print(f"Gen {i}")
            self.simulateGeneration()

    def simulateGeneration(self):
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
            print(f"Wymieranie na wyspie: {self.ISLANDS[hix].name}")
            self.ISLANDS[hix].nukeRandom(0.8)

        #migracja pomiędzy dwoma wyspami
        #TODO duplikaty mogą wywalić program
        if random.random() < MIGRATION_CHANCE:
            r1 = random.randint(0,self.islandNb-1)
            r2 = random.randint(0,self.islandNb-1)
            if r1 != r2:
                print(f"Migracja pomiędzy {self.ISLANDS[r1].name} a {self.ISLANDS[r2].name}")
                migrantsA = self.ISLANDS[r1].stealMembers(MIGRATING_MEMBERS)
                migrantsB = self.ISLANDS[r2].stealMembers(MIGRATING_MEMBERS)
                for m in migrantsB:
                    self.ISLANDS[r1].putInOrder(m)
                for m in migrantsA:
                    self.ISLANDS[r2].putInOrder(m)

        for ISLAND in self.ISLANDS:
            #wybór rodziców (ruletka)
            parents = ISLAND.select(PARENTS_SIZE)
            #krzyżowanie (OX)
            #metoda Single-Point Crossover
            children = ISLAND.crossover(parents)
            #utworzenie nowej populacji
            new_population = self.createPopulation(ISLAND.population,parents,children)
            ISLAND.population = new_population
            #mutowanie nowej populacji
            ISLAND.mutate(MUTATION_CHANCE)


def test():
    file = "../lab1/TSP_Data/" + sys.argv[1]
    if file[-4] == 'a':
        instance = readData.ReadData(file, True)
    else:
        instance = readData.ReadData(file)

    GA = GeneticAlgorithm(1000,2,instance,0.5)
    GA.simulate()

test()
