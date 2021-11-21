import csv
from pathlib import Path
import matplotlib.pyplot as plt
import os
import utils

file_path_1 = Path(r"C:\Users\ASUS\Desktop\sheet-A.csv")
file_path_2 = Path(r"C:\Users\ASUS\Desktop\sheet-EE.csv")
file_path_3 = Path(r"C:\Users\ASUS\Desktop\python_glaciers")

class Glacier:
    
    def __init__(self, glacier_id, name, unit, lat, lon, code):
        self.glacier_id = glacier_id
        self.name = name
        self.unit = unit
        self.lat = lat
        self.lon = lon
        self.code = code
        self.glacier_measurement = {}
        

        #raise NotImplementedError

    def add_mass_balance_measurement(self, year, mass_balance, boolean):
        #self.measurement = {}
        
        for i in range(len(year)):
            sum_mass = 0
            if boolean[i] == True:
                for i1 in range(len(mass_balance[i])-1):
                    sum_mass += mass_balance[i][i1]
                self[year[i]] = sum_mass
            else:
                sum_mass = mass_balance[i]
                self[year[i]] = sum_mass

        

        #raise NotImplementedError
    def plot_mass_balance(self, output_path):
        raise NotImplementedError

        
class GlacierCollection:

    def __init__(self, file_path):
        #raise NotImplementedError("my test: not implemented!")
        with open(file_path) as A:
            reader_A = csv.reader(A)
            filedata_A = list(reader_A)

            self.glacier = {}            
            for i, row in enumerate(filedata_A):
                if i > 0 and i < len(filedata_A):
                    unit = row[0]                    
                    name = row[1]
                    id = row[2]                    
                    latitude = (float(row[5]))                    
                    longitude = (float(row[6]))                 
                    code =(int(row[7]+row[8]+row[9]))
                    d = Glacier(id, name, unit, latitude, longitude, code)
                    self.glacier[name] = d
                
                

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
            value = []
            self.mass_balance = {}
            for i, row in enumerate(filedata_EE):
                if i > 0 and i < len(filedata_EE):
                    list_Munit.append(row[0])                   
                    list_Mname.append(row[1])                    
                    list_Mid.append(row[2])                   
                    list_year.append(row[3])
                    list_lb.append(row[4])                    
                    list_value.append(row[11])
            for i in range(len(list_Mname)):
                if i < len(list_Mname)-1:
                    if list_Mname[i] != list_Mname[i+1]:
                        year_value, boolean = utils.mass_change(list_Mname[i] , list_Mname, list_year, list_value)
                        year_list = list(year_value.keys())
                        value_list = list(year_value.values())
                        g = Glacier
                        g.add_mass_balance_measurement(self.glacier[list_Mname[i]].glacier_measurement, year_list, value_list, boolean)
                        #self.glacier[list_Mname[i]] = year_mass_balance
                        #print(year_list, value_list, boolean)
                else:
                    year_value, boolean = utils.mass_change(list_Mname[i] , list_Mname, list_year, list_value) 
                    year_list = list(year_value.keys())
                    value_list = list(year_value.values())
                    g = Glacier
                    g.add_mass_balance_measurement(self.glacier[list_Mname[i]].glacier_measurement, year_list, value_list, boolean)
                    #self.glacier[list_Mname[i]] = year_mass_balance
                    #print(year_list, value_list, boolean)
            
            print(self.glacier['ARTESONRAJU'].glacier_measurement)

            #a = 0
            #for i in range(len(self.M_name)):
                #a = 0
                #for j in range(len(self.name)):
                    #if self.M_name[i] == self.name[j]:
                        #a += 1
                #if a == 0:
                    #raise NotImplementedError('All the glaciers should be defined')
            #for i in range(len(filedata_EE)):
                #Glacier.add_mass_balance_measurement(self.year[i],self.value[i])


    def find_nearest(self, lat, lon, n):
        """Get the n glaciers closest to the given coordinates."""
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

        list_keys = list(self.glacier.keys())
        name = []
        last_value = []
        for i in range(len(self.glacier)):
            if self.glacier[list_keys[i]].glacier_measurement != {}:
                measurement = self.glacier[list_keys[i]].glacier_measurement
                # the name of single glacier measurement
                name.append(list_keys[i])
                # the latest measurement value of this glacier
                last_value.append(list(measurement.values())[-1])
                
        a = []
        if reverse == False:
            largest_value = utils.n_max(last_value,n)
            
            for i in range(n):
                key = name[largest_value[i]]
                glacier_object = self.glacier[key]
                a.append(glacier_object)
            return a

        if reverse == True:
            smallest_value = utils.n_min(last_value,n)
            
            for i in range(n):
                key = name[smallest_value[i]]
                glacier_object = self.glacier[key]
                a.append(glacier_object)
            return a    
        
        #raise NotImplementedError


    def summary(self):
        
        list_keys = list(self.glacier.keys())
        year = []
        last_value = []
        for i in range(len(self.glacier)):
            if self.glacier[list_keys[i]].glacier_measurement != {}:
                measurement = self.glacier[list_keys[i]].glacier_measurement
                # the earliest year of single glacier measurement
                year.append(list(measurement.keys())[0])
                # the latest measurement value of this glacier
                last_value.append(list(measurement.values())[-1])
        year.sort()
                
        shunk_rate = utils.calculate_shunk_rate(last_value)
        
        print('This collection has %d glaciers.' % len(self.glacier))
        print('The earliest measurement was in %d.' % year[0])
        print(str(shunk_rate) + "%" + " of glaciers shrunk in their last measurement.")
        
        #raise NotImplementedError


    def plot_extremes(self, output_path):
        
        list_keys = list(self.glacier.keys())
        name = []
        last_value = []
        for i in range(len(self.glacier)):
            if self.glacier[list_keys[i]].glacier_measurement != {}:
                measurement = self.glacier[list_keys[i]].glacier_measurement
                # the name of single glacier measurement
                name.append(list_keys[i])
                # the latest measurement value of this glacier
                last_value.append(list(measurement.values())[-1])

        largest_value = utils.n_max(last_value,1)
        smallest_value = utils.n_min(last_value,1)
        key_largest = name[largest_value[0]]
        key_smallest = name[smallest_value[0]]
        largest_change = self.glacier[key_largest].glacier_measurement
        smallest_change = self.glacier[key_smallest].glacier_measurement


        x1 = list(largest_change.keys())
        y1 = list(largest_change.values())           
        plt.plot(x1, y1, c='b', label = name[largest_value[0]] + "(grew the most)")       
        
        x2 = list(smallest_change.keys())
        y2 = list(smallest_change.values())            
        plt.plot(x2, y2, c='r', label=name[smallest_value[0]] + "(shrunk the most)")
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
#print(c.sort_by_latest_mass_balance(5,False))
#print(c.summary())
print(c.plot_extremes(file_path_3))
#g = Glacier('03292', 'ARTESONRAJU', 'PE', -8.95, -77.62, 534).plot_mass_balance(file_path_3)