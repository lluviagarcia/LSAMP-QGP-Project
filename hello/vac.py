from asyncore import file_dispatcher
import matplotlib.pyplot as plt


energylist = []
with open ("vac1.csv") as file:
    line = file.readline().strip().split()
    while line[0] == "P" :
        energylist.append(line[6])
        line = file.readline().strip().split()
        print(line[0])
        if line == "": 
            print("lineempty")
            break
        
print(energylist)






 