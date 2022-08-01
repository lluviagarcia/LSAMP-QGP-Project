from asyncore import file_dispatcher
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

eventcount = 0
particlecount = 0
energylist = []
with open ("vac10.hepmc") as file:
    line = file.readline().strip().split()              # skip junk lines 
    line = file.readline().strip().split()
    line = file.readline().strip().split()
    line = file.readline().strip().split()
    while line[0] == "E" :                              # Start event count at E
        eventcount += 1
        line = file.readline().strip().split()
        for i in range(7) :                             # skip junk lines
            line = file.readline().strip().split()
            i = +1
        while line[0] == "P" :                     # start particle count at P
            particlecount +=1
            energylist.append(line[6])
            line = file.readline().strip().split()
            line = file.readline().strip().split()
            if len(line) == 0:
                break                                   # Break loop when line is empty

            
print(energylist)
print(particlecount)
print(eventcount)

new_list = list(map(float, energylist))

sns.histplot(data = new_list, color= 'navy', kde= 'true', log_scale=(True,True), bins = 5)    #log scale on both axis

plt.xlabel('Energy')
plt.show()
