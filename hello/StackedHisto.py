from __future__ import print_function

import fastjet as fj
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


#import gzip
def main():
    global f
    global jet_def
    global selector
    global x
    # get the banner out of the way early on
    fj.ClusterSequence.print_banner()
    # print()
    
    # set up our jet definition and a jet selector
    jet_def = fj.JetDefinition(fj.antikt_algorithm, 0.4)
    selector = fj.SelectorPtMin(5.0) & fj.SelectorAbsRapMax(4.5)
    print("jet definition is:",jet_def)
    print("jet selector is:", selector,"\n")
    
    #filename = '../data/single-event.dat'
    filename = 'vac10000.hepmc' 
    filename2 = 'hydro-2D10000.hepmc'

    #read and plot first file 
    f = open(filename,'r')
    allJetsFlat = read_file(f)
    p1 = plot_data(allJetsFlat)
    sns.histplot(data = allJetsFlat, x = x, stat = 'probability', color = 'blueviolet', log_scale=True) #change bin boundaries according to data size and add logscale for larger

    f.close()

    #read and plot second file
    f2 = open(filename2, 'r')
    allJetsFlat = read_file(f2)
    p2 = plot_data(allJetsFlat)
    sns.histplot(data = allJetsFlat, x = x, stat = 'probability', color = 'blue', log_scale=True) #change bin boundaries according to data size and add logscale for larger
    plt.legend(labels = ['w/o medium', 'medium'])

    plt.show()

#---------------------------------------------------------------------
def read_file(file_or_filename):
    global line
    if (isinstance(file_or_filename,str)) : f = open(file_or_filename, 'r')
    else                                  : f = file_or_filename

    iev = 0
    alljets = []
   
    line = f.readline().strip().split()
    line = f.readline().strip().split()
    line = f.readline().strip().split()
    line = f.readline().strip().split()
    

    while line[0] == "E":
        event = read_event(f)           #loop over events, and call particle function
        iev += 1
        if ((len(line)) == 0): break                 
        jets = selector(jet_def(event))
        print("Event {0} has {1} particles".format(iev, len(event)))
            
        alljets.append(jets)

        # for ijet in range(len(jets)):
        #     print("jet {0} pt and mass: {1} {2}".format(ijet, jets[ijet].pt(), jets[ijet].m()))

        # make sure jet-related information is correctly held
        if (len(jets) > 0):
            print("Number of constituents of jets[0] is {0}".format(len(jets[0].constituents())))

    #Flatten list of tuples aka open ziplock bags
    global allJetsFlat
    allJetsFlat = list(sum(alljets,()))
    print(len(allJetsFlat))
    global mass
    mass = []
    for iallJetsFlat in range(len(allJetsFlat)):
        #print("jet {0} pt and mass: {1} {2}".format(iallJetsFlat, allJetsFlat[iallJetsFlat].pt(), allJetsFlat[iallJetsFlat].m()))
        mass.append(allJetsFlat[iallJetsFlat].m())
    return allJetsFlat
#----------------------------------------------------------------------
def read_event(file_or_filename):
    global line
    
    if (isinstance(file_or_filename,str)) : f = open(file_or_filename, 'r')
    else                                  : f = file_or_filename
    
    
    
    event = []
    for i in range(9) :                             # skip junk lines
        line = f.readline().strip().split()
        i = +1
        #print(line)
    while line[0] == "P" :                          # start particle count at P
        px,py,pz,e = float(line[3]),float(line[4]),float(line[5]),float(line[6])          #create tuple and turn elements into float values
        event.append(fj.PseudoJet(px,py,pz,e));                                #fill in empty list AND append pseudojets
        line = f.readline().strip().split()
        #if len(line) == 0:
            #break                                   # Break loop when P ends
            
    return event                                        #where this is at matters

#----------------------------------------------------------------------------
def plot_data(allJetsFlat):
    global x
    axis_font = {'fontname':'Times New Roman', 'size':'13'}
    x = mass
    #sns.histplot(data = allJetsFlat, x = x, stat = 'probability', bins = [0,5,10,15,20,25,30]) #change bin boundaries according to data size and add logscale for larger
    plt.xlabel('Jet Mass [GEV]', **axis_font)
    plt.ylabel(r'$\frac{1}{N_jets}\frac{dN}{dM_J}$', **axis_font);
    plt.text(12000,0.025, 'anti-kt  R=0.4')
    plt.text(12000,0.023, ' $p^{jet}\geq5$ GEV ')


if __name__ == '__main__':
    main()

