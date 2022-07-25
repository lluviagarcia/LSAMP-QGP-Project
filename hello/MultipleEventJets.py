from __future__ import print_function

import fastjet as fj
#import gzip

def main():

    # get the banner out of the way early on
    fj.ClusterSequence.print_banner()
    print()

    # set up our jet definition and a jet selector
    jet_def = fj.JetDefinition(fj.antikt_algorithm, 0.4)
    selector = fj.SelectorPtMin(5.0) & fj.SelectorAbsRapMax(4.5)
    print("jet definition is:",jet_def)
    print("jet selector is:", selector,"\n")

    #filename = '../data/single-event.dat'
    filename = 'vac10.hepmc'
    f = open(filename,'r')
    #filename = '/Users/gsalam/work/fastjet/data/Pythia-PtMin50-LHC-10kev.dat.gz'
    #f = gzip.GzipFile(filename,'rb')
    
    # get the event
    iev = 0
    while True:
        event = read_event(f)
        iev += 1
        if (len(event) == 0): break
        jets = selector(jet_def(event))
        print("Event {0} has {1} particles".format(iev, len(event)))
        
        # cluster it
        for ijet in range(len(jets)):
            print("jet {0} pt and rap: {1} {2}".format(ijet, jets[ijet].pt(), jets[ijet].rap()))
            
        # make sure jet-related information is correctly held
        if (len(jets) > 0):
            print("Number of constituents of jets[0] is {0}".format(len(jets[0].constituents())))
            
#----------------------------------------------------------------------
def read_event(file_or_filename):
    """
Routine that can take either an existing opened file object, or a
filename (which it will open itself) and then reads an event from that
file. An event is deemed to end when the file comes to an end or when
the reader encounters the string "#END".

The event is converted to a python list of PseudoJets
    """
eventcount = 0
particlecount = 0
event = []
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
            px,py,e = float(line[3]),float(line[4]),float(line[6])          #create tuple and turn elements into float values
            line = file.readline().strip().split()
            particlesid = [px,py,e]
            event.append(particlesid)                                #fill in empty list AND append pseudojets
            if len(line) == 0:
                break                                   # Break loop when line is empty
    
if __name__ == '__main__':
    main()
