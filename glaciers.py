import csv
from pathlib import Path
import matplotlib.pyplot as plt
import utils




class Glacier:
    def __init__(self, glacier_id, name, unit, lat, lon, code):
        raise NotImplementedError

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
            list_type = []            
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
            self.latitude = list_latitude

            for i, row in enumerate(filedata_A):
                if i > 0 and i < len(filedata_A):
                    list_longitude.append(row[6])
            self.longitude = list_longitude

            for i, row in enumerate(filedata_A):
                if i > 0 and i < len(filedata_A):
                    list_type.append(row[7]+row[8]+row[9])
            self.type = list_type

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
            self.annual_balance = list_ab

    def find_nearest(self, lat, lon, n):
        """Get the n glaciers closest to the given coordinates."""
        if type(n) != int:
            n = 5
        if n > len(self.name):
            raise NotImplementedError('n should not be over the number of glacier')
        distance = []
        for i in range(len(self.latitude)):
            la = float(self.latitude[i])
            lo = float(self.longitude[i])
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
            for i in range(len(self.type)):
                if code_pattern[0] == self.type[i][0]:
                    id1.append(self.name[i])
        else:
            id1 = self.name

        if code_pattern[1] != '?':
            for i in range(len(self.type)):
                if code_pattern[1] == self.type[i][1]:
                    id2.append(self.name[i])
        else:
            id2 = self.name

        if code_pattern[2] != '?':
            for i in range(len(self.type)):
                if code_pattern[2] == self.type[i][2]:
                    id3.append(self.name[i])
        else:
            id3 = self.name
        
        return list(set(id1).intersection(id2,id3))

    def sort_by_latest_mass_balance(self, n, reverse):
        """Return the N glaciers with the highest area accumulated in the last measurement."""     
        #if reverse == False:
           

        #raise NotImplementedError

    def summary(self):
        
        y = self.year.sort()
        print('The earliest measurement was in %d', y[0])
        print('This collection has %d glaciers', len(self.name))
        #raise NotImplementedError

    def plot_extremes(self, output_path):
        raise NotImplementedError
    
    