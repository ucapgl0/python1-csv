import math
import heapq
import matplotlib.pyplot as plt


def haversine_distance(lat1, lon1, lat2, lon2): # Use in calculating nearest glaciers
    """Return the distance in km between two points around the Earth.
    
    Latitude and longitude for each point are given in degrees.
    """
    R = 6371
    arcs = math.asin
    s = math.sin
    c = math.cos
    d = 2*R*arcs(math.sqrt(s((lat2-lat1)/2)**2 + c(lat1)*c(lat2)*(s((lon2-lon1)/2)**2)))
    return d

    raise NotImplementedError


def n_min(list1, n): 
    # Use in find_nearest() and reverse condition of sort_by_latest_mass_balance() and plot_extremes()
    
    max_num_index_list = map(list1.index, heapq.nsmallest(n, list1))

    return list(max_num_index_list)


def n_max(list1, n): 
    # Use in sort_by_latest_mass_balance() and plot_extremes()

    max_num_index_list = map(list1.index, heapq.nlargest(n, list1))

    return list(max_num_index_list)


def create_name_LastMeasurement_dict(name, year, value): 
    # Use in sort_by_latest_mass_balance() and summary() and plot_extremes()
    d = {}
    for i in range(len(name)):
        if value[i] == '':
            value[i] = 0
        s = 0
        if i < len(name) - 1:
            if name[i] != name[i+1]:
                for i1 in range(i, 0, -1):
                    if year[i1] != year[i1-1]:
                        if i1 != i:
                            for j in range(i1,i):
                                s += float(value[j])
                            d[name[i]] = s
                            s = 0
                            break
                        else:
                            d[name[i]] = float(value[i1])
                            break
        else:
            for i2 in range(i, 0, -1):
                    if year[i2] != year[i2-1]:
                        if i2 != i:
                            for j in range(i2,i):
                                s += float(value[j])
                            d[name[i]] = s
                            s = 0
                            break
                        else:
                            d[name[i]] = float(value[i2])
                            break      
    return d
  

def find_key(dictionary,value1): 
    # Use in sort_by_latest_mass_balance() 
    for key in dictionary:
        if dictionary[key] == value1:
            return key


def return_object(Object_name, glacier_id, name, unit, lat, lon, code): 
    # Use in sort_by_latest_mass_balance() 
    for i in range(len(name)):
        if name[i] == Object_name:
            return [glacier_id[i], name[i], unit[i], lat[i], lon[i], code[i]]


def calculate_shunk_rate(list1):
    # Use for summary()
    a = 0
    for i in range(len(list1)):
        if list1[i] < 0:
            a += 1
    b = a / len(list1)
    c = int(round(b,2) * 100)
    return c


def mass_change(Object_name, name, year, value):
    
    a = []
    d = {}
    for i in range(len(name)):
        if name[i] == Object_name:
            a.append(i)  
    a1 = a[0]
    a2 = a[len(a)-1]
    for i1 in range(a1, a2):
        if value[i1] == '':
            value[i1] = 0
    c = -1
    s = 0
    for i2 in range(a1, a2 + 1):
        if i2 < a2:
            c += 1
            if year[i2] != year[i2+1]:            
                if c >= 1:
                    for j in range(i2-c, i2):
                        s += float(value[j])
                    d[int(year[i2])] = s 
                    c = -1
                    s = 0
                else:
                    d[int(year[i2])] = float(value[i2]) 
                    c = -1
        else:
            if year[i2] != year[i2-1]:
                d[int(year[i2])] = float(value[i2]) 
    
    return d


def plot(dictionary):
        
    return plt.show()

        

    