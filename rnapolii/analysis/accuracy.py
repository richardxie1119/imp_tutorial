#!/usr/bin/env python

'''accuracy.py
This script calculates the average accuracy of the structures in a cluster
It uses the IMP.pmi.analysis.Precision class
Requires a native structure for comparison
'''

import IMP
import IMP.pmi
import IMP.pmi.analysis
import IMP.pmi.output
import IMP.atom
import glob
import itertools



# common settings
test_mode = False                             # run on every 10 rmf files
rmfs=glob.glob('kmeans_*_1/cluster.0/*.rmf3') # list of the RMFS to calculate on

# choose components for the precision calculation
# key is the named precision item
# value is a list of selection tuples
selections={"Rpb4":["Rpb4"],
            "Rpb7":["Rpb7"],
            "Rpb4_Rpb7":["Rpb4","Rpb7"]}


##############################
# don't change anything below
##############################

# setup Precision calculator
model=IMP.Model()
frames=[0]*len(rmfs)
model=IMP.Model()
pr=IMP.pmi.analysis.Precision(model,selection_dictionary=selections)
pr.set_precision_style('pairwise_rmsd')
pr.add_structures(zip(rmfs,frames),"ALL")

# calculate average distance to the reference file
pr.set_reference_structure("../data/native.rmf3",0)
print pr.get_average_distance_wrt_reference_structure("ALL")
