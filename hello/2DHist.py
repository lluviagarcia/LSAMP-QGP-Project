import fastjet as fj
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


eventcount = 0          
particlecount = 0
particles = []

with open ("vac10.hepmc") as file:
    line = file.readline().strip().split()              # skip junk lines 
    line = file.readline().strip().split()
    line = file.readline().strip().split()
    line = file.readline().strip().split()
    while line[0] == "E" :                              # Start event count at E
        eventcount += 1
        line = file.readline().strip().split()
        for i in range(8) :                             # skip junk lines
            line = file.readline().strip().split()
            i = +1
        while line[0] == "P" :                          # start particle count at P
            particlecount +=1
            px,py,e = float(line[3]),float(line[4]),float(line[6])           #create tuple and turn elements into float values
            line = file.readline().strip().split()
            particlesid = [px,py,e]
            particles.append(particlesid)                                   #fill in empty list
            if line[0] == "E" :
            #if len(line) == 0:
                break                                   # Break loop when line is empty
print(particles)                                      # Prints Particles list of tuples
# print(particlecount)
# print(eventcount)
# x_value = [x[0] for x in particles]
# y_value = [x[1] for x in particles]
# #plt.style.use('dark_background')
# sns.histplot(data = particles, x = x_value, y = y_value, cbar=True, log_scale=(True,True), cmap='magma')
# plt.xlabel('px')
# plt.ylabel('py')

# plt.show()