from GA import GeneticAlgorithm
import sys
from readData import ReadData
if sys.argv.__len__()!= 5:
    print('plik,liczba generacji,najlepsze PRD,stosunek k:nn')
    sys.exit(1)
file,gen_number,best_PRD,ratio = sys.argv[1:]
instance,invert = (ReadData(file,True),False) if file[-4] == 'a' else (ReadData(file),True)

ox = 1
spx = 3
cx = 4
island_nb = 2
r_cross = 0.5
ga = GeneticAlgorithm(int(gen_number), island_nb,instance,0.5,cx,invert,float(ratio))
imp = ga.simulate(int(best_PRD),True)
