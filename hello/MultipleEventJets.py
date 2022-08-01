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
        
    # get the event
    iev = 0
    line = f.readline().strip().split()
    line = f.readline().strip().split()
    line = f.readline().strip().split()
    line = f.readline().strip().split()
    while line[0] == "E":
        event = read_event(f)           #loop over events, call particle function
        iev += 1
        if (len(event) == 0): break                 #fix infinite loop here?yes
        #if iev== 11 :                                 #chage back to 11
            #break
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
    if (isinstance(file_or_filename,str)) : f = open(file_or_filename, 'r')
    else                                  : f = file_or_filename
    
    event = []
    for i in range(8) :                             # skip junk lines
        line = f.readline().strip().split()
        i = +1
        #print(line)
        while line[0] == "P" :                          # start particle count at P
            px,py,pz,e = float(line[3]),float(line[4]),float(line[5]),float(line[6])          #create tuple and turn elements into float values
            event.append(fj.PseudoJet(px,py,pz,e));                                #fill in empty list AND append pseudojets
            line = f.readline().strip().split()
            if len(line) == 0:
                break                                   # Break loop when P ends
            
    return event                                        #where this is at matters
if __name__ == '__main__':
    main()
