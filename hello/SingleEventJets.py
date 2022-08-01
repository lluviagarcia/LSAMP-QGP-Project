from __future__ import print_function
import fastjet as fj
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#import gzip

def main():


    # set up our jet definition and a jet selector
    jet_def = fj.JetDefinition(fj.antikt_algorithm, 0.6)
    selector = fj.SelectorPtMin(5.0) & fj.SelectorAbsRapMax(4.5)

    filename = 'vac1.hepmc'
    print("I'm here")

    # get the event
    event = read_event(filename)
    print(event)
    # cluster it
    jets = selector(jet_def(event))

    # print out some information about the event and clustering
    print("Event has {0} particles".format(len(event)))
    print("jet definition is:",jet_def)
    print("jet selector is:", selector,"\n")
    
    # print the jets
    print_jets(jets)
    
    # get internal information about one of the jets
    if (len(jets) > 0):
        print("Number of constituents of jets[0] is {0}".format(len(jets[0].constituents())))

#----------------------------------------------------------------------
def print_jets(jets):
    print("{0:>5s} {1:>10s} {2:>10s} {3:>10s}".format("jet #", "pt", "rap", "phi"))
    for ijet in range(len(jets)):
        print("{0:5d} {1:10.3f} {2:10.4f} {3:10.4f}".format(
            ijet, jets[ijet].pt(), jets[ijet].rap(), jets[ijet].phi()))
    
        
#----------------------------------------------------------------------

def read_event(filename):
    event = []
    with open ("vac1.hepmc") as file:
        for i in range(11) :                             # skip junk lines
            line = file.readline().strip().split()
        print(line)
        while line[0] == "P" :                       # start particle count at P
            px,py,pz,e = float(line[3]),float(line[4]),float(line[5]),float(line[6])           #create tuple and turn elements into float values
            event.append(fj.PseudoJet(px,py,pz,e));                                              #fill in empty list
            line = file.readline().strip().split()
            if len(line) == 0:
                break                                   # Break loop when line is empty
        return event

if __name__ == '__main__':
    main()
