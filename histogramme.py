from matplotlib.ticker import FuncFormatter
import pylab
import numpy as np
import matplotlib.pyplot as plt
import random
import file_manager as fm

# Varaibles pour les données 
trafic = list()
stations = list()
quartiers = list()


# Récupération de données sur l'arrondissments de Paris
for elem in fm.data_to_use:
    stations.append(elem[1])
    trafic.append(int(elem[2]))
    quartiers.append(elem[4])


dic_quartiers = dict()
trafic_dic = dict()

for elem in quartiers:
    if not not elem:
        if elem not in dic_quartiers.keys():
            dic_quartiers[elem] = 1
        else:
            dic_quartiers[elem] += 1

for elem in fm.data_to_use:
    if(elem[4]):
        if (elem[4] not in trafic_dic.keys()):
            trafic_dic[elem[4]] = int(elem[2])
        else:
            trafic_dic[elem[4]] += int(elem[2])

print("=====================================")
print("Trafic données : ")
print(trafic_dic)

for key, value in trafic_dic.items():
    print(str(key) + ' -> ' + str(value))


trafic_keys = list(int(key) for key in trafic_dic.keys())
trafic_values = list(trafic_dic.values())


def millions(x, pos):
    'The two args are the value and tick position'
    return '%1.1fM' % (x * 1e-6)

formatrer = FuncFormatter(millions)
fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatrer)

plt.bar(trafic_keys, trafic_values, ec="black")
plt.xlabel('Arrondissements')
plt.ylabel('Taux trafics')
plt.title('Histogram trafic dans Paris')
plt.xticks(trafic_keys)
plt.show()



'''
NUM_FAMILIES = 10

# set the random seed (for reproducibility)
random.seed(42)

# setup the plot
fig, ax = plt.subplots()

# generate some random data
x = [random.randint(0, 5) for x in range(NUM_FAMILIES)]

# create the histogram
ax.hist(x, align='left') # `align='left'` is used to center the labels

# now, define the ticks (i.e. locations where the labels will be plotted)
xticks = [i for i in range(NUM_FAMILIES)]


# also define the labels we'll use (note this MUST have the same size as `xticks`!)
xtick_labels = ['Family-%d' % (f+1) for f in range(NUM_FAMILIES)]

# add the ticks and labels to the plot
ax.set_xticks(xticks)
ax.set_xticklabels(xtick_labels,rotation = 45, ha="right")
plt.show()
'''


'''
names = [stations[i] for i in range(5)]
values = [trafic[i] for i in range(5)]

plt.bar(stations, trafic)
#n, bins, patches = plt.hist(trafic ,bins=50, color='g', alpha=0.75)
plt.xlabel('Stations')
plt.ylabel('Trafic')
plt.title('Histogram trafic')
plt.grid()
plt.show()
'''

'''
# the histogram of the data
n, bins, patches = plt.hist([10, 20], 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
'''