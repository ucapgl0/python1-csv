import csv
from pathlib import Path
import matplotlib.pyplot as plt
import utils


file_path_1 = Path(r"C:\Users\ASUS\Desktop\sheet-A.csv")
file_path_2 = Path(r"C:\Users\ASUS\Desktop\sheet-EE.csv")


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
    

    def add_mass_balance_measurement(self, year, mass_balance, boolean):
        
        if year not in list(self.keys()):
            self[year] = mass_balance
        elif year in list(self.keys()):
            if boolean == True:
                self[year] += mass_balance
        
     

    def plot_mass_balance(self, output_path):

        x = list(self.glacier_measurement.keys())
        y = list(self.glacier_measurement.values())
        plt.plot(x, y, c='y')
        plt.title('Mass balance measurements against the years for %s' % self.name)
        plt.xlabel('Year')
        plt.ylabel('Mass_balance')
        
        plt.savefig(output_path)  # save the plot
        plt.show()
        


        
class GlacierCollection:

    def __init__(self, file_path):
        
        with open(file_path) as A:
            reader_A = csv.reader(A)
            filedata_A = list(reader_A)

            self.glacier = {}            
            for i, row in enumerate(filedata_A):

                if i > 0:
                    # Check the id
                    if row[2].isdigit() == False:
                        raise TypeError('ID is comprised of digits.')
                    if len(row[2]) != 5:
                        raise ValueError('The lenth of ID is 5')

                    # Check the latitude and longitude
                    if row[5].isdigit() == False and row[5][0] != '-' and '.' not in row[5]:
                        raise TypeError('The latitude should be number')
                    if row[6].isdigit() == False and row[6][0] != '-' and '.' not in row[6]:
                        raise TypeError('The longiitude should be number')
                    if float(row[5]) < -90 or float(row[5]) > 90 or float(row[6]) < -180 or float(row[6]) > 180:
                        raise ValueError('The latitude should be between -90 and 90, the longitude between -180 and 180.')

                    # Check the unit
                    if row[0].isupper() == False and row[0] != '99':
                        raise TypeError('unit composed only of capital letters or the special value ”99”.')
                    if len(row[0]) != 2 :
                        raise ValueError('The political unit is a string of length 2') 
                    
                    # Check the code
                    if (row[7]+row[8]+row[9]).isdigit() == False:
                        raise TypeError('The code shoud be 3-digit number.')
                    if len(row[7]+row[8]+row[9]) != 3:
                        raise ValueError('The lenth of code should be 3')

                    unit = row[0]                    
                    name = row[1]
                    id = row[2]                    
                    latitude = float(row[5])                    
                    longitude = (float(row[6]))                 
                    code = (int(row[7]+row[8]+row[9]))
                    self.glacier[id] = Glacier(id, name, unit, latitude, longitude, code)
                
          

    def read_mass_balance_data(self, file_path):
        
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
                    
                    # Check the year
                    if row[3].isdigit == False:
                        raise TypeError('The year should be a number.')
                    if int(row[3]) > 2021:
                        raise ValueError('The year could not be in future.')
                    
                    # Check the lower bound
                    if row[4].isdigit() == False:
                        raise TypeError('The lower bound should be a number.')
                    if float(row[4]) > 9999:
                        raise ValueError('The lower bound should not be over 9999')

                    # read the data if the mass balance is not empty(improper)
                    if row[11] != '':                        
                        # Check the mass balance value
                        if row[11].isdigit() == False and row[11][0] != '-':
                            raise TypeError('The mass balance value should be a number.')
                                                
                        list_Munit.append(row[0])                   
                        list_Mname.append(row[1])                    
                        list_Mid.append(row[2])                   
                        list_year.append(int(row[3]))
                        list_lb.append(row[4])                    
                        list_value.append(float(row[11]))
                                  
            # Check all name, unit and id of glaciers in measurement have already been defined correctly
            v = list(self.glacier.values())
            for i in range(len(list_Mname)):
                a = 0
                for j in range(len(self.glacier)):
                    if list_Mname[i] == v[j].name and list_Mid[i] == v[j].id and list_Munit[i] == v[j].unit:
                        a += 1
                if a == 0:
                    raise ValueError('All the glaciers should be defined correctly.')
            
            
            for i in range(len(list_Mid)):
                if list_lb == '9999':
                    g.add_mass_balance_measurement(self.glacier[list_Mid[i]].glacier_measurement, list_year[i], list_value[i], False)
                else:
                    g.add_mass_balance_measurement(self.glacier[list_Mid[i]].glacier_measurement, list_year[i], list_value[i], True)
            

            
    def find_nearest(self, lat, lon, n):
        
        if n > len(self.glacier):
            raise TypeError('n should not be over the number of glacier')
        if type(lat) != float and type(lat) != int:
            raise TypeError('The latitude should be number')
        if type(lon) != float and type(lon) != int:
            raise TypeError('The longiitude should be number')
        if lat < -90 or lat > 90 or lon < -180 or lon > 180:
            raise ValueError('the latitude should be between -90 and 90, the longitude between -180 and 180')
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
            
        if type(code_pattern) != str:
            raise TypeError("The type of code_pattern should be string")
        if code_pattern.isdigit() == False and '?' not in code_pattern:
            raise TypeError("The code_pattern should only include numbers and '?'") 
        if len(code_pattern) != 3:
            raise ValueError("The length of code_pattern should be 3")

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
        
        name = list(set(id1).intersection(id2,id3))
        # Convenient to test by sort
        name.sort()
        return name



    def sort_by_latest_mass_balance(self, n, reverse):
        
        if n > len(self.glacier):
            raise ValueError('n should not be over the number of object.')
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
        if bool(reverse) == False:
            largest_value = utils.n_max(latest_value,n)
            
            for i in range(n):
                key = id[largest_value[i]]
                glacier_object = self.glacier[key]
                a.append(glacier_object)
            return a

        if bool(reverse) == True:
            smallest_value = utils.n_min(latest_value,n)
            
            for i in range(n):
                key = id[smallest_value[i]]
                glacier_object = self.glacier[key]
                a.append(glacier_object)
            return a   
               


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
        
        # Sort the years to find the earliest year
        year.sort()

        # Calcualte the shunk rate
        shunk_numbers = 0
        for i in range(len(latest_value)):
            if latest_value[i] < 0:
                shunk_numbers += 1
        shunk_rate = shunk_numbers / len(latest_value)
        shunk_percentage = int(round(shunk_rate,2) * 100)  
        
        print('This collection has %d glaciers.' % len(self.glacier))
        print('The earliest measurement was in %d.' % year[0])
        return str(shunk_percentage) + "%" + " of glaciers shrunk in their last measurement."
        


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
        
        plt.savefig(output_path)  # save the plot        
        plt.show()



#Some check

c = GlacierCollection(file_path_1)
c.read_mass_balance_data(file_path_2)
#print(c.filter_by_code('6?6'))
#print(c.find_nearest(-30,-70.5,5))
#print(c.sort_by_latest_mass_balance(7,False))
#print(c.summary())
#print(c.plot_extremes(file_path))
#Glacier.plot_mass_balance(c.glacier['03292'], file_path)


