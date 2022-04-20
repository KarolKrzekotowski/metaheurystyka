import pandas as pd
import matplotlib.pyplot as plt

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True
#
# headers = ['k', 'Prd','time']
#
# df = pd.read_csv('Wyniki3/berlin52.tspwyniki.csv')
# df.
#
# df.set_index('k').plot()
# 'Wyniki3/random_instance_file.atsp0wyniki.csv'
#
# plt.show()
import pandas as pd
fields = ['k', 'time1','prd1','time2', 'prd2']
headers = ['k', 'time1', 'prd1','time2', 'prd2']
#tsp
# berlin = pd.read_csv('Wyniki3/berlin52.tspwyniki.csv', skipinitialspace=True,names=headers, usecols=fields,sep=';')
# ch150 = pd.read_csv('Wyniki3/ch150.tspwyniki.csv', skipinitialspace=True,names=headers, usecols=fields,sep=';')
# gr120 = pd.read_csv('Wyniki3/gr120.tspwyniki.csv', skipinitialspace=True,names=headers, usecols=fields,sep=';')
# pcb442 = pd.read_csv('Wyniki3/pcb442.tspwyniki.csv', skipinitialspace=True,names=headers, usecols=fields,sep=';')
# #atsp
# br17 = pd.read_csv('Wyniki3/br17.atspwyniki.csv', skipinitialspace=True,names=headers, usecols=fields,sep=';')
# ft53 = pd.read_csv('Wyniki3/ft53.atspwyniki.csv', skipinitialspace=True,names=headers, usecols=fields,sep=';')
# ftv170 = pd.read_csv('Wyniki3/ftv170.atspwyniki.csv', skipinitialspace=True,names=headers, usecols=fields,sep=';')
# rbg323 = pd.read_csv('Wyniki3/rbg323.atspwyniki.csv', skipinitialspace=True,names=headers, usecols=fields,sep=';')
# See the keys

# See content in 'star_name'

tsp0 = pd.read_csv('Wyniki3/random_instance_file.tsp0wyniki.csv', skipinitialspace=True,names=headers, usecols=fields,sep=';')
tsp1 = pd.read_csv('Wyniki3/random_instance_file.tsp1wyniki.csv', skipinitialspace=True,names=headers, usecols=fields,sep=';')
tsp2 = pd.read_csv('Wyniki3/random_instance_file.tsp2wyniki.csv', skipinitialspace=True,names=headers, usecols=fields,sep=';')
tsp3 = pd.read_csv('Wyniki3/random_instance_file.tsp3wyniki.csv', skipinitialspace=True,names=headers, usecols=fields,sep=';')
#atsp
atsp0 = pd.read_csv('Wyniki3/random_instance_file.atsp0wyniki.csv', skipinitialspace=True,names=headers, usecols=fields,sep=';')
atsp1 = pd.read_csv('Wyniki3/random_instance_file.atsp1wyniki.csv', skipinitialspace=True,names=headers, usecols=fields,sep=';')
atsp2 = pd.read_csv('Wyniki3/random_instance_file.atsp2wyniki.csv', skipinitialspace=True,names=headers, usecols=fields,sep=';')
atsp3 = pd.read_csv('Wyniki3/random_instance_file.atsp3wyniki.csv', skipinitialspace=True,names=headers, usecols=fields,sep=';')


# plt.plot(berlin.k,berlin.prd1, label='berlin52random', color='green')
# plt.plot(ch150.k,ch150.prd1, label='ch150random', color='orange')
# plt.plot(gr120.k,gr120.prd1, label='gr120random', color='black')
# plt.plot(pcb442.k,pcb442.prd1, label='pcb442random', color='yellow')
#
# plt.plot(berlin.k,berlin.prd2, label='berlin52NN', color='red')
# plt.plot(ch150.k,ch150.prd2, label='ch150NN', color='pink')
# plt.plot(gr120.k,gr120.prd2, label='gr120NN', color='purple')
# plt.plot(pcb442.k,pcb442.prd2, label='pcb442NN', color='blue')
# #atsp
# plt.plot(br17.k,br17.prd1, label='br17random', color='green')
# plt.plot(ch150.k,ft53.prd1, label='ft53random', color='orange')
# plt.plot(gr120.k,ftv170.prd1, label='ftv170random', color='black')
# plt.plot(pcb442.k,rbg323.prd1, label='rbg323random', color='yellow')
#
# plt.plot(br17.k,br17.prd2, label='br17NN', color='red')
# plt.plot(ch150.k,ft53.prd2, label='ft53NN', color='pink')
# plt.plot(gr120.k,ftv170.prd2, label='ftv170NN', color='purple')
# plt.plot(pcb442.k,rbg323.prd2, label='rbg323NN', color='blue')

plt.plot(tsp0.k,tsp0.prd1, label='tsp0Random', color='orange')
plt.plot(tsp1.k,tsp1.prd1, label='tsp1random', color='green')
plt.plot(tsp2.k,tsp2.prd1, label='tsp2random', color='yellow')
plt.plot(tsp3.k,tsp3.prd1, label='tsp3random', color='black')

plt.plot(tsp0.k,tsp0.prd2, label='tsp0random', color='pink')
plt.plot(tsp1.k,tsp1.prd2, label='tsp1random', color='red')
plt.plot(tsp2.k,tsp2.prd2, label='tsp2random', color='blue')
plt.plot(tsp3.k,tsp3.prd2, label='tsp3random', color='purple')


# #atsp
plt.plot(atsp0.k,atsp0.prd1, label='atsp0NN', color='red')
plt.plot(atsp1.k,atsp1.prd1, label='atsp1NN', color='pink')
plt.plot(atsp2.k,atsp2.prd1, label='atsp2NN', color='purple')
plt.plot(atsp3.k,atsp3.prd1, label='atsp3NN', color='blue')

plt.plot(atsp0.k,atsp0.prd2, label='atsp0NN', color='green')
plt.plot(atsp1.k,atsp1.prd2, label='atsp1NN', color='orange')
plt.plot(atsp2.k,atsp2.prd2, label='atsp2NN', color='black')
plt.plot(atsp3.k,atsp3.prd2, label='atsp3NN', color='yellow')




# plt.legend(loc = 'left')
plt.title('(k = 10)Random vs NN, PRD - 100prób')
plt.ylim(ymin=0)
plt.xlim(xmin =0)
plt.savefig('Wykresy3/krandom-vs-NN-PRD-generowane-tsp,atsp.png')
plt.show()
