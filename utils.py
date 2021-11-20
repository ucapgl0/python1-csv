import math
import heapq

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


def create_name_LastMeasurement_dict(name, value): 
    # Use in sort_by_latest_mass_balance() and summary() and plot_extremes()
    d = {}
    for i in range(len(name)):
        if value[i] == '':
            value[i] = 0
        if i < len(name) - 1:
            if name[i] != name[i+1]:
                d[name[i]] = float(value[i])
        else:
            d[name[i]] = float(value[i])
    return d
     

def find_key(dictionary,value1): 
    # Use for sort_by_latest_mass_balance() 
    for key in dictionary:
        if dictionary[key] == value1:
            return key


def return_object(Object_name, glacier_id, name, unit, lat, lon, code): 
    # Use for sort_by_latest_mass_balance() 
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
    for i in range(a1, a2):
        if value[i] == '':
            value[i] = 0
    c = -1
    s = 0
    for i in range(a1, a2):
        if i < a2 - 1:
            c += 1
            if year[i] != year[i+1]:
                if c >= 1:
                   for j in range(i-c, i):
                        s += value[j]
                   d[year[i]] = s
                   c = -1
                else:
                   d[year[i]] = value[i]
                   c = -1
        else:
            if year[i] != year[i-1]:
                d[year[i]] = value[i]
        return d

        

    