import HTPredBenchCreator
from enum import Enum

class CELL(Enum):
    TSMC = 'tsmc_cells/'
    SYNOPSIS = 'synopsis_cells/'

input_file = 'I:/b19_scan.v'

#r = HTPredBenchCreator.Creator(input_file,CELL.TSMC.value, 's15850')
#outpf = 'I:/benchoutput.bench'
#s = open(outpf,'w')
#s.write(r.convert())
#s.close()
#print(r.convert())

r = HTPredBenchCreator.FeatureExtractor(input_file, CELL.SYNOPSIS.value,'b19')
export_file = 'I:/b19_feature.csv'
r.getfeatures(export_file,['preferences/mux_list.txt'])
