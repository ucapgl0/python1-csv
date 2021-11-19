import csv
from pathlib import Path
import matplotlib.pyplot as plt
import utils

file_path_1 = Path(r"C:\Users\ASUS\Desktop\python_glaciers\sheet-A.csv")
file_path_2 = Path(r"C:\Users\ASUS\Desktop\python_glaciers\sheet-EE.csv")

class Glacier:
    def __init__(self, glacier_id, name, unit, lat, lon, code):
        self.id = glacier_id
        self.name = name
        self.unit = unit
        self.lat = lat
        self.lon = lon
        self.code = code
        self.measurement = {}
        #raise NotImplementedError

    def add_mass_balance_measurement(self, year, mass_balance, boolean):
        raise NotImplementedError

    def plot_mass_balance(self, output_path):
        raise NotImplementedError

        
class GlacierCollection:

    def __init__(self, file_path):
        #raise NotImplementedError("my test: not implemented!")
        with open(file_path) as A:
            reader_A = csv.reader(A)
            filedata_A = list(reader_A)
            list_unit = []
            list_name = []
            list_id = []
            list_latitude = []
            list_longitude = []
            list_code = []            
            for i, row in enumerate(filedata_A):
                if i > 0 and i < len(filedata_A):
                    list_unit.append(row[0])
            self.unit = list_unit

            for i, row in enumerate(filedata_A):
                if i > 0 and i < len(filedata_A):
                    list_name.append(row[1])
            self.name = list_name

            for i, row in enumerate(filedata_A):
                if i > 0 and i < len(filedata_A):
                    list_id.append(row[2])
            self.id = list_id

            for i, row in enumerate(filedata_A):
                if i > 0 and i < len(filedata_A):
                    list_latitude.append(row[5])
            self.lat = list_latitude

            for i, row in enumerate(filedata_A):
                if i > 0 and i < len(filedata_A):
                    list_longitude.append(row[6])
            self.lon = list_longitude

            for i, row in enumerate(filedata_A):
                if i > 0 and i < len(filedata_A):
                    list_code.append(row[7]+row[8]+row[9])
            self.code = list_code
            
            #for i in range(len(filedata_A)):
                #Glacier(self.id[0],self.name[0],self.unit[0],self.latitude[0],self.longitude[0],self.code[0])
            

    def read_mass_balance_data(self, file_path):
        #raise NotImplementedError
        with open(file_path) as EE:
            reader_EE = csv.reader(EE)
            filedata_EE = list(reader_EE)
            list_Munit = []
            list_Mname = []
            list_Mid = []
            list_year = []
            list_lb = []
            list_ub = []
            list_ab = []
            for i, row in enumerate(filedata_EE):
                if i > 0 and i < len(filedata_EE):
                    list_Munit.append(row[0])
            self.M_unit = list_Munit

            for i, row in enumerate(filedata_EE):
                if i > 0 and i < len(filedata_EE):
                    list_Mname.append(row[1])
            self.M_name = list_Mname

            for i, row in enumerate(filedata_EE):
                if i > 0 and i < len(filedata_EE):
                    list_Mid.append(row[2])
            self.M_id = list_Mid

            for i, row in enumerate(filedata_EE):
                if i > 0 and i < len(filedata_EE):
                    list_year.append(row[3])
            self.year = list_year

            for i, row in enumerate(filedata_EE):
                if i > 0 and i < len(filedata_EE):
                    list_lb.append(row[4])
            self.lb = list_lb

            for i, row in enumerate(filedata_EE):
                if i > 0 and i < len(filedata_EE):
                    list_ub.append(row[5])
            self.ub = list_ub

            for i, row in enumerate(filedata_EE):
                if i > 0 and i < len(filedata_EE):
                    list_ab.append(row[11])
            self.value = list_ab
            
            #for i in range(len(filedata_EE)):
                #Glacier.add_mass_balance_measurement(self.year[i],self.value[i])


    def find_nearest(self, lat, lon, n):
        """Get the n glaciers closest to the given coordinates."""
        if type(n) != int:
            n = 5
        if n > len(self.name):
            raise NotImplementedError('n should not be over the number of glacier')
        distance = []
        for i in range(len(self.lat)):
            la = float(self.lat[i])
            lo = float(self.lon[i])
            distance.append(utils.haversine_distance(lat,lon,la,lo))

        a = utils.n_min(distance,n)
        name = []
        for i in range(n):
            name.append(self.name[a[i]])

        return name 

    def filter_by_code(self, code_pattern):
        """Return the names of glaciers whose codes match the given pattern."""
        if len(code_pattern) != 3:
            raise NotImplementedError("The length of code_pattern should be 3")
        if type(code_pattern) != str:
            raise NotImplementedError("The type of code_pattern should be string")
        if code_pattern.isdigit() == False and '?' not in code_pattern:
            raise NotImplementedError("The code_pattern should only include numbers and '?'") 
        id1 = []
        id2 = []
        id3 = []
        if code_pattern[0] != '?':
            for i in range(len(self.code)):
                if code_pattern[0] == self.code[i][0]:
                    id1.append(self.name[i])
        else:
            id1 = self.name

        if code_pattern[1] != '?':
            for i in range(len(self.code)):
                if code_pattern[1] == self.code[i][1]:
                    id2.append(self.name[i])
        else:
            id2 = self.name

        if code_pattern[2] != '?':
            for i in range(len(self.code)):
                if code_pattern[2] == self.code[i][2]:
                    id3.append(self.name[i])
        else:
            id3 = self.name
        
        return list(set(id1).intersection(id2,id3))

    def sort_by_latest_mass_balance(self, n, reverse):
        """Return the N glaciers with the highest area accumulated in the last measurement."""
             
        dict = utils.create_name_LastMeasurement_dict(self.M_name, self.value)
        list_value = list(dict.values()) 

        a = []
        if reverse == False:
            most_value = utils.n_max(list_value,n)
            
            for i in range(n):
                b = utils.find_key(dict,list_value[most_value[i]])
                c = utils.return_object(b, self.id, self.name, self.unit, self.lat, self.lon, self.code)
                a.append(c)
            return a

        if reverse == True:
            most_value = utils.n_min(list_value,n)
            
            for i in range(n):
                b = utils.find_key(dict,list_value[most_value[i]])
                c = utils.return_object(b, self.id, self.name, self.unit, self.lat, self.lon, self.code)
                a.append(c)
            return a       
        

        #raise NotImplementedError

    def summary(self):
        
        y = sorted(self.year)
        print('This collection has %d glaciers' % len(self.name))
        print('The earliest measurement was in %d' % int(y[0]))
        
        #raise NotImplementedError

    def plot_extremes(self, output_path):
        raise NotImplementedError
    
c = GlacierCollection(file_path_1)
c.read_mass_balance_data(file_path_2)
#print(c.filter_by_code('4?6'))
#print(c.find_nearest(-30,-70,5))
print(c.sort_by_latest_mass_balance(5,False))
#print(c.summary())