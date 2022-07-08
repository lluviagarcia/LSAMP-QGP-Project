from asyncore import file_dispatcher
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

energylist = []
with open ("vac1.csv") as file:
    line = file.readline().strip().split()
    while line[0] == "P" :
        energylist.append(line[6])
        line = file.readline().strip().split()
        if len(line) == 0: 
            break
new_list = list(map(float, energylist))


sns.histplot(data = new_list, color= 'navy', kde= 'true', log_scale=True)
plt.xlabel('Energy')
plt.show()

