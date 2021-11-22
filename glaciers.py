import csv
from pathlib import Path
import matplotlib.pyplot as plt
import os

import utils

file_path_1 = Path(r"C:\Users\ASUS\Desktop\sheet-A.csv")
file_path_2 = Path(r"C:\Users\ASUS\Desktop\sheet-EE.csv")
file_path_3 = Path(r"C:\Users\ASUS\Desktop\21080370")


n = 5

class Glacier:
    
    def __init__(self, glacier_id, name, unit, lat, lon, code):
        self.id = glacier_id
        self.name = name
        self.unit = unit
        self.lat = lat
        self.lon = lon
        self.code = code
        self.glacier_measurement = {}
    #raise NotImplementedError

    def add_mass_balance_measurement(self, year, mass_balance, boolean):
        #self.measurement = {}
        if year not in list(self.keys()):
            self[year] = mass_balance
        elif year in list(self.keys()):
            if boolean == True:
                self[year] += mass_balance
               
        #raise NotImplementedError

    def plot_mass_balance(self, output_path):

        x = list(self.glacier_measurement.keys())
        y = list(self.glacier_measurement.values())
        plt.plot(x, y, c='y')
        plt.title('Mass balance measurements against the years for %s' % self.name)
        plt.xlabel('Year')
        plt.ylabel('Mass_balance')
        my_path = os.path.abspath(output_path) # Figures out the path
        my_file = 'Plot for glacier %s.png' % self.name # file name
        plt.savefig(os.path.join(my_path, my_file))  # save the plot
        plt.show()
        #raise NotImplementedError


        
class GlacierCollection:

    def __init__(self, file_path):
        #raise NotImplementedError("my test: not implemented!")
        with open(file_path) as A:
            reader_A = csv.reader(A)
            filedata_A = list(reader_A)

            self.glacier = {}            
            for i, row in enumerate(filedata_A):

                if i > 0:
                    # Check the id
                    if len(row[2]) != 5 or row[2].isdigit() == False:
                        raise NotImplementedError('ID is comprised of exactly 5 digits.')
                    # Check the latitude and longitude
                    if float(row[5]) < -90 or float(row[5]) > 90 or float(row[6]) < -180 or float(row[6]) > 180:
                        raise NotImplementedError('The latitude should be between -90 and 90, the longitude between -180 and 180.')
                    # Check the unit
                    if len(row[0]) != 2 or (row[0].isupper() == False and row[0] != '99'):
                        raise NotImplementedError('The political unit is a string of length 2, composed only of capital letters or the special value ”99”.') 
                    # Check the code
                    if len(row[7]+row[8]+row[9]) != 3 or (row[7]+row[8]+row[9]).isdigit() == False:
                        raise NotImplementedError('The code shoud be 3-digit number.')
                    unit = row[0]                    
                    name = row[1]
                    id = row[2]                    
                    latitude = float(row[5])                    
                    longitude = (float(row[6]))                 
                    code = (int(row[7]+row[8]+row[9]))
                    self.glacier[id] = Glacier(id, name, unit, latitude, longitude, code)
                
          


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
            list_value = []
            g = Glacier
            for i, row in enumerate(filedata_EE):
                if i > 0:
                    if int(row[3]) > 2021:
                        raise NotImplementedError('The year could not be in future.')
                    
                    if row[11] != '':
                        # read the data if the mass balance is not empty(improper)
                        list_Munit.append(row[0])                   
                        list_Mname.append(row[1])                    
                        list_Mid.append(row[2])                   
                        list_year.append(int(row[3]))
                        list_lb.append(row[4])                    
                        list_value.append(float(row[11]))
                                  
            # Check all glacier measurement have already been defined correctly
            v = list(self.glacier.values())
            for i in range(len(list_Mname)):
                a = 0
                for j in range(len(self.glacier)):
                    if list_Mname[i] == v[j].name and list_Mid[i] == v[j].id and list_Munit[i] == v[j].unit:
                        a += 1
                if a == 0:
                    raise NotImplementedError('All the glaciers should be defined correctly.')
            
            
            for i in range(len(list_Mid)):
                if list_lb == '9999':
                    g.add_mass_balance_measurement(self.glacier[list_Mid[i]].glacier_measurement, list_year[i], list_value[i], False)
                else:
                    g.add_mass_balance_measurement(self.glacier[list_Mid[i]].glacier_measurement, list_year[i], list_value[i], True)
            

            
    def find_nearest(self, lat, lon, n):
        
        if type(n) != int:
            n = 5
        if n > len(self.glacier):
            raise NotImplementedError('n should not be over the number of glacier')
        if lat < -90 or lat > 90 or lon < -180 or lon > 180:
            raise NotImplementedError('the latitude should be between -90 and 90, the longitude between -180 and 180')
        distance = []
        list_key = list(self.glacier.keys())
        for i in range(len(self.glacier)):
            la = float(self.glacier[list_key[i]].lat)
            lo = float(self.glacier[list_key[i]].lon)
            distance.append(utils.haversine_distance(lat,lon,la,lo))

        a = utils.n_min(distance,n)
        name = []
        for i in range(n):
            name.append(self.glacier[list_key[a[i]]].name)

        return name 
    


    def filter_by_code(self, code_pattern):
        
        if len(code_pattern) != 3:
            raise NotImplementedError("The length of code_pattern should be 3")
        if type(code_pattern) != str:
            raise NotImplementedError("The type of code_pattern should be string")
        if code_pattern.isdigit() == False and '?' not in code_pattern:
            raise NotImplementedError("The code_pattern should only include numbers and '?'") 
        id1 = []
        id2 = []
        id3 = []
        list_key = list(self.glacier.keys())
        if code_pattern[0] != '?':
            for i in range(len(self.glacier)):
                if code_pattern[0] == str(self.glacier[list_key[i]].code)[0]:
                    id1.append(self.glacier[list_key[i]].name)
        else:
            for i in range(len(self.glacier)):
                id1.append(self.glacier[list_key[i]].name)

        if code_pattern[1] != '?':
            for i in range(len(self.glacier)):
                if code_pattern[1] == str(self.glacier[list_key[i]].code)[1]:
                    id2.append(self.glacier[list_key[i]].name)
        else:
            for i in range(len(self.glacier)):
                id2.append(self.glacier[list_key[i]].name)

        if code_pattern[2] != '?':
            for i in range(len(self.glacier)):
                if code_pattern[2] == str(self.glacier[list_key[i]].code)[2]:
                    id3.append(self.glacier[list_key[i]].name)
        else:
            for i in range(len(self.glacier)):
                id3.append(self.glacier[list_key[i]].name)
        
        return list(set(id1).intersection(id2,id3))



    def sort_by_latest_mass_balance(self, n, reverse):
        """Return the N glaciers with the highest area accumulated in the last measurement."""
        if n > len(self.glacier):
            raise NotImplementedError('n should not be over the number of object.')
        list_keys = list(self.glacier.keys())
        id = []
        latest_value = []
        for i in range(len(self.glacier)):
            if self.glacier[list_keys[i]].glacier_measurement != {}:
                measurement = self.glacier[list_keys[i]].glacier_measurement
                # the name of single glacier measurement
                id.append(list_keys[i])
                # the latest measurement value of this glacier
                latest_value.append(list(measurement.values())[-1])
                
        a = []
        if reverse == False:
            largest_value = utils.n_max(latest_value,n)
            
            for i in range(n):
                key = id[largest_value[i]]
                glacier_object = self.glacier[key]
                a.append(glacier_object)
            return a

        if reverse == True:
            smallest_value = utils.n_min(latest_value,n)
            
            for i in range(n):
                key = id[smallest_value[i]]
                glacier_object = self.glacier[key]
                a.append(glacier_object)
            return a    
        
        #raise NotImplementedError


    def summary(self):
        
        list_keys = list(self.glacier.keys())
        year = []
        latest_value = []
        for i in range(len(self.glacier)):
            if self.glacier[list_keys[i]].glacier_measurement != {}:
                measurement = self.glacier[list_keys[i]].glacier_measurement
                # the earliest year of single glacier measurement
                year.append(list(measurement.keys())[0])
                # the latest measurement value of this glacier
                latest_value.append(list(measurement.values())[-1])
        year.sort()
                
        shunk_rate = utils.calculate_shunk_rate(latest_value)
        
        print('This collection has %d glaciers.' % len(self.glacier))
        print('The earliest measurement was in %d.' % year[0])
        return str(shunk_rate) + "%" + " of glaciers shrunk in their last measurement."
        
        #raise NotImplementedError


    def plot_extremes(self, output_path):
        
        list_keys = list(self.glacier.keys())
        id = []
        latest_value = []
        for i in range(len(self.glacier)):
            if self.glacier[list_keys[i]].glacier_measurement != {}:
                measurement = self.glacier[list_keys[i]].glacier_measurement
                # the name of single glacier measurement
                id.append(list_keys[i])
                # the latest measurement value of this glacier
                latest_value.append(list(measurement.values())[-1])
        
        largest_value = utils.n_max(latest_value,1)
        smallest_value = utils.n_min(latest_value,1)
        key_largest = id[largest_value[0]]
        key_smallest = id[smallest_value[0]]
        largest_change = self.glacier[key_largest].glacier_measurement
        smallest_change = self.glacier[key_smallest].glacier_measurement

        x1 = list(largest_change.keys())
        y1 = list(largest_change.values())           
        plt.plot(x1, y1, c='b', label = self.glacier[id[largest_value[0]]].name + "(grew the most)")       
        
        x2 = list(smallest_change.keys())
        y2 = list(smallest_change.values())            
        plt.plot(x2, y2, c='r', label= self.glacier[id[smallest_value[0]]].name + "(shrunk the most)")
        plt.title('Mass balance measurements against the years for two extreme glaciers')
        plt.xlabel('Year')
        plt.ylabel('Mass_balance')
        plt.legend()

        my_path = os.path.abspath(output_path) # Figures out the path
        my_file = 'Plot for two extreme glaciers.png' # file name
        plt.savefig(os.path.join(my_path, my_file))  # save the plot
        
        plt.show()
        
        #raise NotImplementedError



c = GlacierCollection(file_path_1)
c.read_mass_balance_data(file_path_2)
#print(c.filter_by_code('6?8'))
#print(c.find_nearest(-30,-70,5))
print(c.sort_by_latest_mass_balance(n,False))
#print(c.summary())
#print(c.plot_extremes(file_path_3))
#Glacier.plot_mass_balance(c.glacier['REMBESDALSKAAKA'], file_path_3)
#print(list(c.glacier.keys())[1694])

