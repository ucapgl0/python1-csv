import csv
from pathlib import Path
import glaciers
import pytest

#import utils
#test
file_path_1 = Path(r"C:\Users\ASUS\Desktop\python_glaciers\sheet-A.csv")
file_path_2 = Path(r"C:\Users\ASUS\Desktop\python_glaciers\sheet-EE.csv")
glaciers.GlacierCollection(file_path_1)
#print(g.filter_by_code('4?6'))
#print(g.find_nearest(-30,-70,5))
#print(g.sort_by_latest_mass_balance(5,0))
print(glaciers.GlacierCollection.summary)

file_path = Path(r"C:\Users\ASUS\Desktop\python_glaciers\sheet-A.csv")
with open(file_path) as A:
    reader = csv.reader(A)
    filedata = list(reader)
    for j in filedata:
        k = j[2:3]
    a = []
    b = []
    j = 0 
    k = 0            
    for i, row in enumerate(filedata):
        #if i < len(filedata):
        if row[0] == 'AR':
            a.append(float(row[5]))
            
    #print(sum(a))
            #print(row[5])
        if 0 < i and i < len(filedata):
            b.append(row[7]+row[8]+row[9])
            
    #print(b[2][0])
                
    

        
