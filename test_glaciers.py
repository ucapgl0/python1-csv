import csv
from pathlib import Path
import glaciers

#import utils
#test
file_path_1 = Path(r"C:\Users\ASUS\Desktop\python_glaciers\sheet-A.csv")
file_path_2 = Path(r"C:\Users\ASUS\Desktop\python_glaciers\sheet-EE.csv")
g = glaciers.GlacierCollection(file_path_1,file_path_2)
#print(g.filter_by_code('4?6'))
#print(g.find_nearest(-30,-70,5))
#print(g.sort_by_latest_mass_balance(5,0))
print(g.summary())


    

        
